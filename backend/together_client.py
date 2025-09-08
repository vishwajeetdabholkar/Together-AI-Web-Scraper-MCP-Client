from together import Together
from typing import List, Dict, Any
import os
import logging

logger = logging.getLogger(__name__)

class TogetherAIClient:
    def __init__(self):
        api_key = os.getenv('TOGETHER_API_KEY')
        if not api_key:
            raise ValueError("TOGETHER_API_KEY environment variable is required")
            
        self.client = Together(api_key=api_key)
        self.model = "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8"
    
    def chat_with_tools(self, messages: List[Dict], tools: List[Dict] = None):
        """Send chat request with optional tools to Together AI"""
        try:
            logger.info(f"Sending request to {self.model} with {len(tools) if tools else 0} tools")
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=tools if tools else [],
                stream=False
            )
            
            logger.info("Received response from Together AI")
            return response
            
        except Exception as e:
            logger.error(f"Together AI API error: {e}")
            raise