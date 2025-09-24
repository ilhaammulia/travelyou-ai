import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
    OPENWEBUI_API_URL = os.getenv("OPENWEBUI_API_URL")
    OPENWEBUI_API_KEY = os.getenv("OPENWEBUI_API_KEY")
    OPENWEBUI_API_MODEL = os.getenv("OPENWEBUI_API_MODEL", "llama3.2:1b")
    SECRET_KEY = os.getenv("SECRET_KEY", "dev")

    RATE_LIMIT = int(os.getenv("RATE_LIMIT", 5))
    TIME_WINDOW = int(os.getenv("TIME_WINDOW", 60))

