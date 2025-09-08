# AI Web Scraper Pro Configuration

## Environment Configuration

This directory contains configuration files for different environments and deployment scenarios.

### Files

- `development.env` - Development environment configuration
- `production.env` - Production environment configuration
- `docker.env` - Docker-specific configuration

## Usage

Copy the appropriate configuration file to the project root as `.env`:

```bash
# For development
cp config/development.env .env

# For production
cp config/production.env .env

# For Docker
cp config/docker.env .env
```

## Configuration Options

### MCP Server Configuration
- `MCP_SERVER_COMMAND` - Command to run MCP server (default: python)
- `MCP_SERVER_PATH` - Path to MCP server script

### Together AI Configuration
- `TOGETHER_API_KEY` - Your Together AI API key
- `TOGETHER_MODEL` - Model to use (default: meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8)

### Flask Configuration
- `FLASK_PORT` - Port for Flask API (default: 9000)
- `FLASK_DEBUG` - Enable debug mode (default: false)
- `FLASK_HOST` - Host to bind to (default: 0.0.0.0)

### Logging Configuration
- `LOG_LEVEL` - Logging level (DEBUG, INFO, WARNING, ERROR)
- `LOG_FILE` - Log file path (default: logs/app.log)

### Security Configuration
- `SECRET_KEY` - Secret key for Flask sessions
- `CORS_ORIGINS` - Allowed CORS origins (comma-separated)

## Environment-Specific Settings

### Development
- Debug mode enabled
- Detailed logging
- Hot reload enabled
- CORS allows all origins

### Production
- Debug mode disabled
- Optimized logging
- Security headers enabled
- Restricted CORS origins

### Docker
- Optimized for containerized deployment
- Environment-specific paths
- Container networking configuration
