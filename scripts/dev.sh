#!/bin/bash

# AI Web Scraper Pro - Development Utilities

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Project root directory
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo -e "${BLUE}🚀 AI Web Scraper Pro - Development Utilities${NC}"
echo "=============================================="

# Function to show usage
show_usage() {
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  setup     - Set up development environment"
    echo "  test      - Run all tests"
    echo "  lint      - Run code linting"
    echo "  format    - Format code"
    echo "  security  - Run security checks"
    echo "  clean     - Clean up temporary files"
    echo "  logs      - Show recent logs"
    echo "  status    - Show system status"
    echo ""
}

# Setup development environment
setup_dev() {
    echo -e "${YELLOW}📦 Setting up development environment...${NC}"
    
    # Create virtual environment if it doesn't exist
    if [ ! -d "venv" ]; then
        echo "Creating virtual environment..."
        python -m venv venv
    fi
    
    # Activate virtual environment
    source venv/bin/activate
    
    # Install dependencies
    echo "Installing dependencies..."
    pip install -r requirements.txt
    
    # Install development dependencies
    pip install pytest pytest-cov flake8 bandit black isort
    
    # Create .env file if it doesn't exist
    if [ ! -f ".env" ]; then
        echo "Creating .env file from template..."
        cp env.example .env
        echo -e "${YELLOW}⚠️  Please edit .env file with your API keys${NC}"
    fi
    
    echo -e "${GREEN}✅ Development environment setup complete!${NC}"
}

# Run tests
run_tests() {
    echo -e "${YELLOW}🧪 Running tests...${NC}"
    cd "$PROJECT_ROOT"
    
    if [ -d "venv" ]; then
        source venv/bin/activate
    fi
    
    pytest tests/ --cov=backend --cov-report=html --cov-report=term-missing
    echo -e "${GREEN}✅ Tests completed!${NC}"
}

# Run linting
run_lint() {
    echo -e "${YELLOW}🔍 Running code linting...${NC}"
    cd "$PROJECT_ROOT"
    
    if [ -d "venv" ]; then
        source venv/bin/activate
    fi
    
    echo "Running flake8..."
    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
    flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    
    echo -e "${GREEN}✅ Linting completed!${NC}"
}

# Format code
format_code() {
    echo -e "${YELLOW}🎨 Formatting code...${NC}"
    cd "$PROJECT_ROOT"
    
    if [ -d "venv" ]; then
        source venv/bin/activate
    fi
    
    echo "Running black..."
    black .
    
    echo "Running isort..."
    isort .
    
    echo -e "${GREEN}✅ Code formatting completed!${NC}"
}

# Run security checks
run_security() {
    echo -e "${YELLOW}🔒 Running security checks...${NC}"
    cd "$PROJECT_ROOT"
    
    if [ -d "venv" ]; then
        source venv/bin/activate
    fi
    
    echo "Running bandit..."
    bandit -r backend/ -f json -o logs/security-report.json || true
    
    echo -e "${GREEN}✅ Security checks completed!${NC}"
    echo "Security report saved to logs/security-report.json"
}

# Clean up temporary files
clean_files() {
    echo -e "${YELLOW}🧹 Cleaning up temporary files...${NC}"
    cd "$PROJECT_ROOT"
    
    # Remove Python cache files
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -name "*.pyc" -delete 2>/dev/null || true
    
    # Remove test coverage files
    rm -rf htmlcov/ .coverage .pytest_cache/ 2>/dev/null || true
    
    # Remove log files
    rm -f logs/*.log 2>/dev/null || true
    
    echo -e "${GREEN}✅ Cleanup completed!${NC}"
}

# Show recent logs
show_logs() {
    echo -e "${YELLOW}📋 Recent logs:${NC}"
    cd "$PROJECT_ROOT"
    
    if [ -f "logs/backend.log" ]; then
        echo -e "${BLUE}Backend logs (last 20 lines):${NC}"
        tail -20 logs/backend.log
    fi
    
    if [ -f "logs/streamlit.log" ]; then
        echo -e "${BLUE}Streamlit logs (last 20 lines):${NC}"
        tail -20 logs/streamlit.log
    fi
}

# Show system status
show_status() {
    echo -e "${YELLOW}📊 System Status:${NC}"
    cd "$PROJECT_ROOT"
    
    # Check if services are running
    if curl -s http://localhost:9000/health > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Backend API: Running${NC}"
    else
        echo -e "${RED}❌ Backend API: Not running${NC}"
    fi
    
    if curl -s http://localhost:8501 > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Streamlit UI: Running${NC}"
    else
        echo -e "${RED}❌ Streamlit UI: Not running${NC}"
    fi
    
    # Show disk usage
    echo -e "${BLUE}💾 Disk Usage:${NC}"
    du -sh . 2>/dev/null || echo "Unable to calculate disk usage"
}

# Main script logic
case "${1:-}" in
    setup)
        setup_dev
        ;;
    test)
        run_tests
        ;;
    lint)
        run_lint
        ;;
    format)
        format_code
        ;;
    security)
        run_security
        ;;
    clean)
        clean_files
        ;;
    logs)
        show_logs
        ;;
    status)
        show_status
        ;;
    *)
        show_usage
        exit 1
        ;;
esac
