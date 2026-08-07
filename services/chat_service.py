from memory.memory_manager import MemoryManager
from providers.ollama_provider import OllamaProvider


class ChatService:

    def __init__(self):
        self.provider = OllamaProvider()
        self.memory = MemoryManager()

    def ask(self, question: str):

        prompt = self.memory.build_prompt(question)

        answer = self.provider.chat(prompt)

        self.memory.add("user", question)
        self.memory.add("assistant", answer)

        return answer

    def stream(self, question: str):

        prompt = self.memory.build_prompt(question)

        complete_answer = ""

        for chunk in self.provider.stream_chat(prompt):
            complete_answer += chunk
            yield chunk

        self.memory.add("user", question)
        self.memory.add("assistant", complete_answer)

    def clear_memory(self):
        self.memory.clear()

    def history(self):
        return self.memory.get_history()