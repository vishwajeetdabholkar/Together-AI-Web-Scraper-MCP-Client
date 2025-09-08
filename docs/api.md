# API Documentation

## Overview

The AI Web Scraper Pro API provides endpoints for intelligent web content analysis using Together AI and MCP integration.

## Base URL

- **Development**: `http://localhost:9000`
- **Production**: `https://your-domain.com`

## Authentication

Currently, no authentication is required. In production, consider implementing API keys or OAuth.

## Endpoints

### Health Check

Check if the API is running and healthy.

```http
GET /health
```

**Response:**
```json
{
  "status": "healthy"
}
```

### Chat with AI

Send a message to the AI for analysis and processing.

```http
POST /chat
Content-Type: application/json

{
  "message": "Analyze the content of https://example.com"
}
```

**Response:**
```json
{
  "response": "Based on the content analysis...",
  "tool_used": true,
  "tool_results": "{\"url\": \"https://example.com\", \"title\": \"Example\", ...}"
}
```

### Debug MCP Connection

Test the MCP server connection and list available tools.

```http
GET /debug/mcp
```

**Response:**
```json
{
  "status": "success",
  "tools_count": 2,
  "tools": ["scrape_url", "scrape_search_results"]
}
```

### Debug Together AI

Test the Together AI connection.

```http
GET /debug/together
```

**Response:**
```json
{
  "status": "success",
  "model": "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
  "response": "Hello! I'm ready to help you analyze web content."
}
```

### List Available Tools

Get detailed information about available MCP tools.

```http
GET /debug/tools
```

**Response:**
```json
{
  "status": "success",
  "tools_count": 2,
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "scrape_url",
        "description": "Scrape content from a given URL",
        "parameters": {
          "type": "object",
          "properties": {
            "url": {
              "type": "string",
              "description": "The URL to scrape"
            }
          },
          "required": ["url"]
        }
      }
    }
  ]
}
```

## Error Responses

All endpoints may return error responses in the following format:

```json
{
  "error": "Error message describing what went wrong"
}
```

**Common HTTP Status Codes:**
- `200` - Success
- `400` - Bad Request (invalid input)
- `500` - Internal Server Error

## Rate Limiting

Currently no rate limiting is implemented. Consider implementing rate limiting for production use.

## Examples

### Python Example

```python
import requests

# Health check
response = requests.get("http://localhost:9000/health")
print(response.json())

# Chat with AI
response = requests.post(
    "http://localhost:9000/chat",
    json={"message": "Analyze https://example.com"}
)
result = response.json()
print(result["response"])
```

### cURL Example

```bash
# Health check
curl http://localhost:9000/health

# Chat with AI
curl -X POST http://localhost:9000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Analyze https://example.com"}'
```

## WebSocket Support

Currently not implemented. Future versions may include WebSocket support for real-time communication.
