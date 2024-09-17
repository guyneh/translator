# This script provides functions to interact with OpenAI's GPT-4 and Anthropic's Claude AI models for generating text completions based on a given prompt.

import os
from dotenv import load_dotenv
from openai import OpenAI
import anthropic

# Load environment variables from .env file
load_dotenv()

# Function to interact with OpenAI's GPT-4 model
def chatgpt(prompt, max_tokens=2000, temperature=0.3):
    # Initialize the OpenAI client with the API key from environment variables
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    # Create a chat completion request
    response = client.chat.completions.create(
        model="gpt-4o",
        max_tokens=max_tokens,
        temperature=temperature,
        messages=[{"role": "user", "content": prompt}]
    )
    # Return the generated text from the response
    return response.choices[0].message.content

# Function to interact with Anthropic's Claude AI model
def claude(prompt, max_tokens=2000, temperature=0.3):
    # Initialize the Anthropic client with the API key from environment variables
    client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
    
    # Create a message completion request
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=max_tokens,
        temperature=temperature,
        messages=[{"role": "user", "content": prompt}]
    )
    # Return the generated text from the response
    return response.content[0].text
