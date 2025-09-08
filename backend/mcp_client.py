import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from typing import List, Dict, Any
import os
import logging

logger = logging.getLogger(__name__)

class MCPWebScraperClient:
    def __init__(self):
        # Set the correct path to your scrape server
        self.server_path = os.path.abspath("./scrape_mcp_server.py")
        self.server_command = "python"
        
        # Validate that the server file exists
        if not os.path.exists(self.server_path):
            raise FileNotFoundError(f"MCP server file not found: {self.server_path}")
    
    async def get_available_tools(self) -> List[Dict]:
        """Get list of available tools from MCP server"""
        server_params = StdioServerParameters(
            command=self.server_command,
            args=[self.server_path]
        )
        
        try:
            async with stdio_client(server_params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    result = await session.list_tools()
                    
                    tools = []
                    for tool in result.tools:
                        tools.append({
                            "type": "function", 
                            "function": {
                                "name": tool.name,
                                "description": tool.description,
                                "parameters": tool.inputSchema
                            }
                        })
                    
                    logger.info(f"Found {len(tools)} tools: {[t['function']['name'] for t in tools]}")
                    return tools
                    
        except Exception as e:
            logger.error(f"Failed to get tools: {e}")
            return []
    
    async def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> str:
        """Execute a tool on the MCP server using fresh connection"""
        server_params = StdioServerParameters(
            command=self.server_command,
            args=[self.server_path]
        )
        
        try:
            async with stdio_client(server_params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    
                    logger.info(f"Calling tool {tool_name} with args: {arguments}")
                    result = await session.call_tool(tool_name, arguments)
                    
                    if result.isError:
                        error_msg = result.content[0].text if result.content else 'Unknown error'
                        logger.error(f"Tool error: {error_msg}")
                        return f"Error: {error_msg}"
                    
                    content = result.content[0].text if result.content else "No result"
                    logger.info(f"Tool result length: {len(content)} characters")
                    return content
                    
        except Exception as e:
            logger.error(f"Failed to call tool {tool_name}: {e}")
            return f"Error calling tool: {str(e)}"
    

