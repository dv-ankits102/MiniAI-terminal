import json
import requests

from config import OLLAMA_URL, MODEL_NAME
from providers.base import BaseProvider


class OllamaProvider(BaseProvider):

    def chat(self, prompt: str) -> str:

        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        return response.json()["response"]

    def stream_chat(self, prompt: str):

        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": True
            },
            stream=True,
            timeout=120
        )

        response.raise_for_status()

        for line in response.iter_lines():

            if not line:
                continue

            data = json.loads(line)

            if "response" in data:
                yield data["response"]

            if data.get("done", False):
                break