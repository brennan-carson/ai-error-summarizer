# summarizer.py

import openai
import os
from dotenv import load_dotenv

# Load .env and get API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(error_lines):
    """
    Sends error lines to OpenAI and returns a summary and root cause analysis.
    """
    if not error_lines:
        return "No error lines provided."

    # Construct prompt
    prompt = (
        "You are an expert system administrator analyzing logs from a distributed system.\n"
        "Here are some error logs:\n\n"
        + "\n".join(error_lines[:50]) +  # limit to first 50 lines to reduce token usage
        "\n\nPlease summarize the main issues and suggest likely root causes."
    )

    # Call GPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "You are a helpful assistant for DevOps teams."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=300
    )

    return response['choices'][0]['message']['content'].strip()

