import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

HOST = "0.0.0.0"
PORT = 8000
API_URL = "http://localhost:8000"