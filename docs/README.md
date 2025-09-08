# AI Web Scraper Pro - Documentation

## 📚 Table of Contents

- [API Documentation](api.md)
- [Deployment Guide](deployment.md)
- [Development Guide](development.md)
- [Troubleshooting](troubleshooting.md)
- [Architecture Overview](architecture.md)

## 🚀 Quick Start

1. **Installation**: See [README.md](../README.md#-quick-start)
2. **Configuration**: Copy `env.example` to `.env` and configure
3. **Running**: Use `./run.sh` for unified startup

## 📖 API Reference

### Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | System health check |
| `/chat` | POST | Send message to AI |
| `/debug/mcp` | GET | Test MCP connection |
| `/debug/together` | GET | Test Together AI connection |
| `/debug/tools` | GET | List available tools |

### Request/Response Examples

See [API Documentation](api.md) for detailed examples.

## 🛠️ Development

### Project Structure

```
ai-web-scraper-pro/
├── backend/          # Flask API server
├── ui/              # Streamlit UI
├── tests/           # Test suite
├── docs/            # Documentation
├── logs/            # Application logs
├── scripts/         # Utility scripts
└── config/          # Configuration files
```

### Running Tests

```bash
pytest tests/
```

### Code Quality

```bash
flake8 .
bandit -r backend/
```

## 🔧 Configuration

### Environment Variables

See [env.example](../env.example) for all available configuration options.

### Logging

Logs are stored in the `logs/` directory:
- `backend.log` - Flask API logs
- `streamlit.log` - Streamlit UI logs

## 📞 Support

- 📧 Email: support@ai-web-scraper-pro.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/ai-web-scraper-pro/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/ai-web-scraper-pro/discussions)
