# orchestrator/gemini_helper.py
from .gemini_config import MODEL

def call_gemini(prompt: str) -> str:
    response = MODEL.generate_content(prompt)
    return response.text.strip()
