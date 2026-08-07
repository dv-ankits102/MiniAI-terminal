from app import chat_service


def execute():

    history = chat_service.history()

    if not history:
        return "No conversation history."

    output = ""

    for item in history:
        output += (
            f"{item['role'].capitalize()}: "
            f"{item['content']}\n\n"
        )

    return output