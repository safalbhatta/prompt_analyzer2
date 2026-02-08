import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = "llama-3.3-70b-versatile"
GROQ_TEMPERATURE = 0.7
GROQ_MAX_TOKENS = 1000
GROQ_TIMEOUT = 30

AVAILABLE_MODELS = {
    "llama-3.3-70b-versatile": "LLaMA 3.3 70B Versatile",
    "llama2-70b-4096": "LLaMA 2 70B",
    "gemma-7b-it": "Gemma 7B"
}

DEFAULT_TEMPERATURE = GROQ_TEMPERATURE
DEFAULT_MAX_TOKENS = GROQ_MAX_TOKENS