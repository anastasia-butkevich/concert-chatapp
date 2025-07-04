import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
API_URL = f"http://{HOST}:{PORT}"
