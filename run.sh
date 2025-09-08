#!/bin/bash

# Together AI MCP Client - Unified Startup Script
# This script starts both the Flask backend and Streamlit UI with unified logging

set -e  # Exit on any error

echo "🚀 Starting Together AI MCP Client..."
echo "=================================="

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "   Please create a .env file with the following content:"
    echo ""
    echo "   # MCP Server Configuration"
    echo "   MCP_SERVER_COMMAND=python"
    echo "   MCP_SERVER_PATH=./scrape_mcp_server.py"
    echo ""
    echo "   # Together AI Configuration"
    echo "   TOGETHER_API_KEY=your_key_here"
    echo ""
    echo "   # Flask Configuration"
    echo "   FLASK_PORT=9000"
    echo ""
    echo "   Continuing without .env file..."
    echo ""
fi

# Check if scrape_mcp_server.py exists
if [ ! -f "scrape_mcp_server.py" ]; then
    echo "❌ Error: scrape_mcp_server.py not found!"
    echo "   Please ensure the MCP server file exists in the project root."
    exit 1
fi

# Check if requirements are installed
echo "📦 Checking dependencies..."
python -c "import flask, streamlit, mcp, together, requests, bs4" 2>/dev/null || {
    echo "❌ Missing dependencies detected!"
    echo "   Please run: pip install -r requirements.txt"
    exit 1
}

echo "✅ Dependencies OK"
echo ""

# Function to cleanup background processes
cleanup() {
    echo ""
    echo "🛑 Shutting down services..."
    if [ ! -z "$BACKEND_PID" ]; then
        kill $BACKEND_PID 2>/dev/null || true
        echo "   Backend stopped"
    fi
    if [ ! -z "$STREAMLIT_PID" ]; then
        kill $STREAMLIT_PID 2>/dev/null || true
        echo "   Streamlit stopped"
    fi
    echo "✅ All services stopped"
    exit 0
}

# Set up signal handlers for graceful shutdown
trap cleanup SIGINT SIGTERM

# Start Flask backend
echo "🔧 Starting Flask backend on port 9000..."
cd backend
python app.py > ../logs/backend.log 2>&1 &
BACKEND_PID=$!
cd ..

# Wait a moment for backend to start
sleep 3

# Check if backend started successfully
if ! kill -0 $BACKEND_PID 2>/dev/null; then
    echo "❌ Backend failed to start!"
    echo "   Check backend.log for details"
    exit 1
fi

echo "✅ Backend started (PID: $BACKEND_PID)"
echo ""

# Start Streamlit UI
echo "🎨 Starting Streamlit UI on port 8501..."
streamlit run ui/streamlit_app.py --server.port 8501 --server.headless true > logs/streamlit.log 2>&1 &
STREAMLIT_PID=$!

# Wait a moment for Streamlit to start
sleep 5

# Check if Streamlit started successfully
if ! kill -0 $STREAMLIT_PID 2>/dev/null; then
    echo "❌ Streamlit failed to start!"
    echo "   Check streamlit.log for details"
    cleanup
    exit 1
fi

echo "✅ Streamlit started (PID: $STREAMLIT_PID)"
echo ""

# Display status
echo "🎉 All services are running!"
echo "=================================="
echo "📊 Backend API:    http://localhost:9000"
echo "🎨 Streamlit UI:   http://localhost:8501"
echo "🔍 Health Check:   http://localhost:9000/health"
echo "🐛 Debug MCP:      http://localhost:9000/debug/mcp"
echo "🐛 Debug Together: http://localhost:9000/debug/together"
echo ""
echo "📝 Logs:"
echo "   Backend:   tail -f logs/backend.log"
echo "   Streamlit: tail -f logs/streamlit.log"
echo "   Combined:  tail -f logs/backend.log logs/streamlit.log"
echo ""
echo "Press Ctrl+C to stop all services"
echo ""

# Monitor both processes
while true; do
    if ! kill -0 $BACKEND_PID 2>/dev/null; then
        echo "❌ Backend process died!"
        cleanup
        exit 1
    fi
    
    if ! kill -0 $STREAMLIT_PID 2>/dev/null; then
        echo "❌ Streamlit process died!"
        cleanup
        exit 1
    fi
    
    sleep 2
done