from collections import deque


class MemoryManager:
    """Stores conversation history."""

    def __init__(self, max_messages: int = 10):
        self.messages = deque(maxlen=max_messages)

    def add(self, role: str, content: str):
        self.messages.append(
            {
                "role": role,
                "content": content,
            }
        )

    def build_prompt(self, user_message: str) -> str:
        prompt = ""

        for message in self.messages:
            prompt += (
                f"{message['role'].capitalize()}: "
                f"{message['content']}\n"
            )

        prompt += f"User: {user_message}\nAssistant:"
        return prompt

    def clear(self):
        self.messages.clear()

    def get_history(self):
        return list(self.messages)