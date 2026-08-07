from commands import chat
from commands import search
from commands import help


class Router:

    def route(self, text: str):

        text = text.strip()

        if text.startswith("/chat "):
            return chat.execute(text[6:])

        elif text.startswith("/search "):
            return search.execute(text[8:])

        elif text == "/help":
            return help.execute()

        elif text == "/exit":
            raise SystemExit

        elif text == "/history":
            from commands import history
            return history.execute()

        elif text == "/clear":
            from commands import clear
            return clear.execute()

        return "Unknown command. Type /help"