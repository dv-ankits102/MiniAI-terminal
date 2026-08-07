from app import chat_service


def execute(prompt: str):

    response = ""

    for token in chat_service.stream(prompt):
        response += token

    return response