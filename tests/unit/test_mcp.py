import pytest
import asyncio
from backend.mcp_client import MCPWebScraperClient

@pytest.mark.asyncio
async def test_mcp_connection():
    """Test MCP server connection"""
    client = MCPWebScraperClient()
    
    try:
        connected = await client.connect()
        assert connected == True
        
        tools = await client.get_available_tools()
        assert len(tools) > 0
        
        print(f"Available tools: {[tool['function']['name'] for tool in tools]}")
        
    finally:
        await client.cleanup()

if __name__ == "__main__":
    asyncio.run(test_mcp_connection())