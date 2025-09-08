import streamlit as st
import requests
import json
import time
from datetime import datetime

# Page configuration - MUST be first Streamlit command
st.set_page_config(
    page_title="AI Web Scraper Pro",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-color: #1f77b4;
        --secondary-color: #ff7f0e;
        --success-color: #2ca02c;
        --danger-color: #d62728;
        --warning-color: #ff7f0e;
        --info-color: #17a2b8;
        --light-color: #f8f9fa;
        --dark-color: #343a40;
    }

    /* Custom header styling */
    .main-header {
        background: linear-gradient(90deg, #1f77b4 0%, #ff7f0e 100%);
        padding: 2rem 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
    }
    
    .main-header p {
        color: white;
        margin: 0.5rem 0 0 0;
        text-align: center;
        font-size: 1.1rem;
        opacity: 0.9;
    }

    /* Chat message styling */
    .chat-message {
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin-left: 20%;
    }
    
    .assistant-message {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        margin-right: 20%;
    }

    /* Status indicators */
    .status-indicator {
        display: inline-block;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        margin-right: 8px;
    }
    
    .status-online {
        background-color: #28a745;
        box-shadow: 0 0 10px rgba(40, 167, 69, 0.5);
    }
    
    .status-offline {
        background-color: #dc3545;
        box-shadow: 0 0 10px rgba(220, 53, 69, 0.5);
    }

    /* Tool usage expander */
    .tool-expander {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }

    /* Sidebar styling */
    .sidebar-content {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }

    /* Metrics cards */
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin: 0.5rem 0;
    }

    /* Loading animation */
    .loading-dots {
        display: inline-block;
    }
    
    .loading-dots::after {
        content: '';
        animation: dots 1.5s steps(4, end) infinite;
    }
    
    @keyframes dots {
        0%, 20% { content: ''; }
        40% { content: '.'; }
        60% { content: '..'; }
        80%, 100% { content: '...'; }
    }

    /* Footer */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: #343a40;
        color: white;
        text-align: center;
        padding: 0.5rem;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
<div class="main-header">
    <h1>🚀 AI Web Scraper Pro</h1>
    <p>Intelligent Web Content Analysis powered by Together AI & MCP</p>
</div>
""", unsafe_allow_html=True)

# Backend configuration
BACKEND_URL = "http://localhost:9000"

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "session_start_time" not in st.session_state:
    st.session_state.session_start_time = datetime.now()

# Sidebar with professional layout
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    
    # System Status
    st.markdown("### 🔧 System Status")
    
    # Backend health check
    backend_status = False
    try:
        health_response = requests.get(f"{BACKEND_URL}/health", timeout=5)
        backend_status = health_response.status_code == 200
    except:
        backend_status = False
    
    status_class = "status-online" if backend_status else "status-offline"
    status_text = "Online" if backend_status else "Offline"
    
    st.markdown(f"""
    <div class="metric-card">
        <div style="display: flex; align-items: center;">
            <span class="status-indicator {status_class}"></span>
            <strong>Backend API:</strong> {status_text}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Session info
    session_duration = datetime.now() - st.session_state.session_start_time
    st.markdown(f"""
    <div class="metric-card">
        <strong>Session Duration:</strong><br>
        {str(session_duration).split('.')[0]}
    </div>
    """, unsafe_allow_html=True)
    
    # Message count
    st.markdown(f"""
    <div class="metric-card">
        <strong>Messages:</strong> {len(st.session_state.messages)}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Quick Actions
    st.markdown("### ⚡ Quick Actions")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧹 Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.session_state.session_start_time = datetime.now()
            st.rerun()
    
    with col2:
        if st.button("🔄 Refresh Status", use_container_width=True):
            st.rerun()
    
    # Debug Tools (collapsible)
    with st.expander("🔧 Debug Tools", expanded=False):
        if st.button("Test MCP Connection"):
            with st.spinner("Testing MCP..."):
                try:
                    debug_response = requests.get(f"{BACKEND_URL}/debug/mcp", timeout=10)
                    if debug_response.status_code == 200:
                        result = debug_response.json()
                        if result.get("status") == "success":
                            st.success(f"✅ MCP: {result['tools_count']} tools available")
                            st.code(result["tools"])
                        else:
                            st.error(f"❌ MCP Error: {result.get('error')}")
                    else:
                        st.error("❌ MCP: Connection failed")
                except Exception as e:
                    st.error(f"❌ MCP Error: {e}")
        
        if st.button("Test Together AI"):
            with st.spinner("Testing Together AI..."):
                try:
                    debug_response = requests.get(f"{BACKEND_URL}/debug/together", timeout=10)
                    if debug_response.status_code == 200:
                        result = debug_response.json()
                        st.success("✅ Together AI: Connected")
                        st.code(result.get("response", ""))
                    else:
                        st.error("❌ Together AI: Connection failed")
                except Exception as e:
                    st.error(f"❌ Together AI Error: {e}")
    
    # About section
    st.markdown("### ℹ️ About")
    st.markdown("""
    **AI Web Scraper Pro** combines:
    - 🤖 **Together AI's Llama 4 Maverick** for intelligent analysis
    - 🔧 **MCP (Model Context Protocol)** for seamless tool integration
    - 🌐 **Advanced web scraping** for content extraction
    
    **Try these examples:**
    - "Analyze the content of https://example.com"
    - "Summarize the main points from [URL]"
    - "Extract key insights from this article: [URL]"
    """)

# Main chat interface
st.markdown("### 💬 Chat Interface")

# Display chat history with professional styling
for i, message in enumerate(st.session_state.messages):
    if message["role"] == "user":
        st.markdown(f"""
        <div class="chat-message user-message">
            <strong>You:</strong><br>
            {message["content"]}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-message assistant-message">
            <strong>AI Assistant:</strong><br>
            {message["content"]}
        </div>
        """, unsafe_allow_html=True)
        
        if message.get("tool_used"):
            with st.expander("🔧 Tool Usage Details", expanded=False):
                st.code(message.get("tool_results", ""), language="json")

# Chat input with enhanced styling
st.markdown("### 📝 New Message")
prompt = st.text_area(
    "Enter a URL to analyze or ask me to summarize web content...",
    height=100,
    placeholder="Example: Analyze the content of https://example.com and provide key insights",
    key="chat_input"
)

if st.button("🚀 Send Message", type="primary", use_container_width=True):
    if prompt.strip():
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Get AI response with enhanced loading
        with st.spinner("🤖 AI is analyzing your request..."):
            try:
                # Call backend
                response = requests.post(
                    f"{BACKEND_URL}/chat",
                    json={"message": prompt},
                    timeout=60
                )
                
                if response.status_code == 200:
                    result = response.json()
                    ai_response = result["response"]
                    tool_used = result.get("tool_used", False)
                    tool_results = result.get("tool_results", "")
                    
                    # Add to chat history
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": ai_response,
                        "tool_used": tool_used,
                        "tool_results": tool_results
                    })
                    
                    st.success("✅ Response received successfully!")
                    st.rerun()
                else:
                    error_msg = f"Error: {response.status_code} - {response.text}"
                    st.error(error_msg)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": error_msg
                    })
                    
            except requests.exceptions.RequestException as e:
                error_msg = f"Connection error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_msg
                })
    else:
        st.warning("Please enter a message before sending.")

# Footer
st.markdown("""
<div class="footer">
    <p>AI Web Scraper Pro | Powered by Together AI & MCP | Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)