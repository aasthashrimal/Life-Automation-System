import os
import google.generativeai as genai

GEMINI_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_KEY:
    raise ValueError("Set GEMINI_API_KEY in environment.")

genai.configure(api_key=GEMINI_KEY)
