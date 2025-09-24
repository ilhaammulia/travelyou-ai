import requests
import json
from config import Config


class LLMRepository:
    def __init__(self):
        self.url = Config.OPENWEBUI_API_URL
        self.headers = {
            "authorization": "Bearer " + Config.OPENWEBUI_API_KEY,
            "content-type": "application/json"
        }

    def extract_query(self, user_prompt: str) -> str:
        system_instruction = """
        You are a personal travel guide that recommend me about itinerary things
        I would like to know about {}
        response with format only the place/restaurant name using **
        """

        payload = {
            "model": Config.OPENWEBUI_API_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": system_instruction.format(user_prompt)
                }
            ]
        }
        try:
            resp = requests.post(self.url + "/chat/completions", json=payload, headers=self.headers, timeout=30).json()
            content = resp['choices'][0]['message']['content']
            return content
        except Exception as err:
            return user_prompt
