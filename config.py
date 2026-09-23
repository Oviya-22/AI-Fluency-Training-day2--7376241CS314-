import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY is not set in the .env file")

client = Groq(api_key=API_KEY)

MODEL = "openai/gpt-oss-20b"


def banner(title):
    print("=" * 72)
    print(title)
    print("=" * 72)