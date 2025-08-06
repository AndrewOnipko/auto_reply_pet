import os
from dotenv import load_dotenv

load_dotenv()

LLM_PROMPT = os.getenv("LLM_PROMPT")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = os.getenv("DEEPSEEK_API_URL")
QUESTIONS_PATH = "questions.json"
AI_MODEL = os.getenv('DEEPSEEK_MODEL')