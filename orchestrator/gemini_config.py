# orchestrator/gemini_config.py
import os
import google.generativeai as genai

GEMINI_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"

if not GEMINI_KEY:
    raise ValueError("Please set GEMINI_API_KEY in your environment.")

def init_model():
    genai.configure(api_key=GEMINI_KEY)
    return genai.GenerativeModel(MODEL_NAME)
