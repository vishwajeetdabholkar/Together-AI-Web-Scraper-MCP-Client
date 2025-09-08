from flask import Flask, request, jsonify
from flask_cors import CORS
import asyncio
import json
import logging
import os
from together_client import TogetherAIClient
from mcp_client import MCPWebScraperClient

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Initialize clients
together_client = TogetherAIClient()
mcp_client = MCPWebScraperClient()

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/debug/mcp', methods=['GET'])
def debug_mcp():
    """Debug MCP connection"""
    try:
        # Test MCP connection - DON'T cleanup after
        result = asyncio.run(test_mcp_connection_no_cleanup())
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

async def test_mcp_connection_no_cleanup():
    """Test MCP server connection without cleanup"""
    try:
        tools = await mcp_client.get_available_tools()
        
        return {
            "status": "success",
            "tools_count": len(tools),
            "tools": [t['function']['name'] for t in tools]
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }
@app.route('/debug/together', methods=['GET'])
def debug_together():
    """Debug Together AI connection"""
    try:
        # Test Together AI connection
        test_messages = [{"role": "user", "content": "Hello, can you respond?"}]
        response = together_client.chat_with_tools(test_messages)
        return jsonify({
            "status": "success",
            "model": together_client.model,
            "response": response.choices[0].message.content
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/debug/tools', methods=['GET'])
def debug_tools():
    """Debug available MCP tools"""
    try:
        tools = asyncio.run(mcp_client.get_available_tools())
        return jsonify({
            "status": "success",
            "tools_count": len(tools),
            "tools": tools
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/chat', methods=['POST'])
def chat():
    try:
        local_mcp_client = MCPWebScraperClient()
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({"error": "No message provided"}), 400
        
        logger.info(f"Processing chat message: {user_message[:100]}...")
        
        # Run async chat processing
        result = asyncio.run(process_chat(user_message, local_mcp_client))
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"Chat error: {e}")
        return jsonify({"error": str(e)}), 500

async def test_mcp_connection():
    """Test MCP server connection"""
    try:
        tools = await mcp_client.get_available_tools()
        
        return {
            "status": "success",
            "tools_count": len(tools),
            "tools": [t['function']['name'] for t in tools]
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }

async def process_chat(user_message: str, mcp_client: MCPWebScraperClient):
    """Process chat message with MCP tools"""
    try:
        # Get available MCP tools
        tools = await mcp_client.get_available_tools()
        logger.info(f"Available tools: {[t['function']['name'] for t in tools]}")
        
        # Prepare messages for Together AI
        messages = [
            {
                "role": "system", 
                "content": "You are a helpful assistant that can scrape and summarize web content. When a user provides a URL or asks to scrape content, use the scrape_url tool. Always provide detailed summaries of the scraped content."
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
        
        # Send to Together AI with tools
        response = together_client.chat_with_tools(messages, tools)
        
        # Check if AI wants to call a tool
        assistant_message = response.choices[0].message
        
        if assistant_message.tool_calls:
            logger.info(f"AI wants to call {len(assistant_message.tool_calls)} tools")
            
            # Execute the tool calls
            tool_results = []
            for tool_call in assistant_message.tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)
                
                logger.info(f"Executing tool: {tool_name}")
                
                # Call the MCP tool
                tool_result = await mcp_client.call_tool(tool_name, tool_args)
                tool_results.append(tool_result)
                
                # Add tool result to messages
                messages.append({
                    "role": "assistant",
                    "content": assistant_message.content or "",
                    "tool_calls": [tool_call.model_dump()]
                })
                
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": tool_result
                })
            
            # Get final response from AI
            final_response = together_client.chat_with_tools(messages)
            
            return {
                "response": final_response.choices[0].message.content,
                "tool_used": True,
                "tool_results": tool_results[0] if tool_results else ""
            }
        else:
            logger.info("No tools called, returning direct response")
            return {
                "response": assistant_message.content,
                "tool_used": False
            }
            
    except Exception as e:
        logger.error(f"Error in process_chat: {e}")
        return {
            "response": f"Sorry, I encountered an error: {str(e)}",
            "tool_used": False,
            "error": str(e)
        }

if __name__ == '__main__':
    app.run(debug=True, port=9000)