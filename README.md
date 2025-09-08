# 🚀 AI Web Scraper Pro

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.29+-red.svg)
![Together AI](https://img.shields.io/badge/together--ai-powered-orange.svg)

**Intelligent Web Content Analysis powered by Together AI & MCP**

[Features](#-features) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 🌟 Overview

AI Web Scraper Pro is a production-grade application that combines the power of **Together AI's Llama 4 Maverick** with **Model Context Protocol (MCP)** to provide intelligent web content analysis and summarization. Built with a modern, professional UI and robust backend architecture.

<img width="1723" height="894" alt="image" src="https://github.com/user-attachments/assets/2727d628-e9d8-4725-882f-41242cdfcf41" />


### 🎯 Key Capabilities

- **Intelligent Web Scraping**: Extract and analyze content from any URL
- **AI-Powered Analysis**: Leverage Together AI's advanced language models
- **Tool Integration**: Seamless MCP integration for extensible functionality
- **Professional UI**: Modern, responsive interface built with Streamlit
- **Production Ready**: Robust error handling, logging, and monitoring

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit UI  │    │   Flask API    │    │   MCP Server   │
│   (Port 8501)   │◄──►│   (Port 9000)   │◄──►│   (Local)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   Together AI   │
                       │   Llama 4       │
                       │   Maverick      │
                       └─────────────────┘
```

## ✨ Features

### 🤖 AI-Powered Analysis
- **Advanced Language Model**: Together AI's Llama 4 Maverick for intelligent responses
- **Context-Aware Processing**: Understands user intent and provides relevant analysis
- **Multi-format Support**: Handles various content types and structures

### 🔧 Tool Integration
- **MCP Protocol**: Model Context Protocol for seamless tool integration
- **Web Scraping Tools**: Extract text, links, and structured data from websites
- **Extensible Architecture**: Easy to add new tools and capabilities

### 🎨 Professional UI
- **Modern Design**: Clean, professional interface with gradient themes
- **Real-time Status**: Live system monitoring and health checks
- **Interactive Chat**: Intuitive chat interface with message history
- **Debug Tools**: Built-in debugging and testing capabilities

### 🚀 Production Features
- **Error Handling**: Comprehensive error management and user feedback
- **Logging**: Detailed logging for monitoring and debugging
- **Health Checks**: System status monitoring and diagnostics
- **Scalable Architecture**: Designed for production deployment

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Together AI API key ([Get one here](https://api.together.xyz/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vishwajeetdabholkar/Together-AI-Web-Scraper-MCP-Client.git
   cd Together-AI-Web-Scraper-MCP-Client
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Use this link to setup locally running eGet-scrapper : 
    ```
    https://github.com/vishwajeetdabholkar/eGet-Crawler-for-ai 
    ```
    All instrctuions are provided inside the repo, just start it using Docker and the mcp_scraper server will work
    
3. **Configure environment**
   ```bash
   cp env.example .env
   # Edit .env and add your Together AI API key
   ```

4. **Start the application**
   ```bash
   ./run.sh
   ```

5. **Access the application**
   - **Web UI**: http://localhost:8501
   - **API**: http://localhost:9000
   - **Health Check**: http://localhost:9000/health

## 📖 Documentation

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | System health check |
| `/chat` | POST | Send message to AI |
| `/debug/mcp` | GET | Test MCP connection |
| `/debug/together` | GET | Test Together AI connection |
| `/debug/tools` | GET | List available tools |

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `TOGETHER_API_KEY` | Together AI API key | Required |
| `MCP_SERVER_COMMAND` | MCP server command | `python` |
| `MCP_SERVER_PATH` | Path to MCP server | `./scrape_mcp_server.py` |
| `FLASK_PORT` | Flask server port | `9000` |

### Usage Examples

**Basic Web Analysis**
```
Analyze the content of https://example.com and provide key insights
```

**Content Summarization**
```
Summarize the main points from https://news-article-url.com
```

**Data Extraction**
```
Extract all links and key information from https://documentation-site.com
```

## 🛠️ Development

### Project Structure

```
ai-web-scraper-pro/
├── backend/                 # Flask API server
│   ├── app.py              # Main Flask application
│   ├── mcp_client.py       # MCP client implementation
│   ├── together_client.py  # Together AI client
│   └── scrape_mcp_server.py # MCP server implementation
├── ui/                     # Streamlit UI
│   └── streamlit_app.py    # Main UI application
├── tests/                  # Test suite
│   ├── unit/               # Unit tests
│   ├── integration/        # Integration tests
│   └── fixtures/           # Test data
├── docs/                   # Documentation
│   ├── api.md             # API documentation
│   └── README.md          # Documentation index
├── logs/                   # Application logs
├── scripts/                # Utility scripts
│   └── dev.sh             # Development utilities
├── config/                 # Configuration files
├── .github/                # GitHub workflows
├── run.sh                  # Unified startup script
└── requirements.txt        # Python dependencies
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=backend --cov-report=html
```

### Code Quality

```bash
# Lint code
flake8 .

# Security check
bandit -r backend/
```

### Development Utilities

Use the development script for common tasks:

```bash
# Set up development environment
./scripts/dev.sh setup

# Run tests
./scripts/dev.sh test

# Format code
./scripts/dev.sh format

# Run linting
./scripts/dev.sh lint

# Security checks
./scripts/dev.sh security

# Show system status
./scripts/dev.sh status

# View logs
./scripts/dev.sh logs
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Run tests: `pytest tests/`
5. Commit changes: `git commit -m 'Add amazing feature'`
6. Push to branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Together AI](https://together.ai/) for providing advanced language models
- [Model Context Protocol](https://modelcontextprotocol.io/) for tool integration
- [Streamlit](https://streamlit.io/) for the amazing UI framework
- [Flask](https://flask.palletsprojects.com/) for the robust API framework
- [eGet-Crawler-for-ai](https://github.com/vishwajeetdabholkar/eGet-Crawler-for-ai) for the powerful web scraping framework that powers our content extraction capabilities

## 📞 Support

- 📧 Email: support@ai-web-scraper-pro.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/ai-web-scraper-pro/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/ai-web-scraper-pro/discussions)

---

<div align="center">

**Made with ❤️ by the AI Web Scraper Pro Team**

[⭐ Star this repo](https://github.com/yourusername/ai-web-scraper-pro) • [🐛 Report Bug](https://github.com/yourusername/ai-web-scraper-pro/issues) • [💡 Request Feature](https://github.com/yourusername/ai-web-scraper-pro/issues)

</div>
