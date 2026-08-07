from app import chat_service


def execute():

    chat_service.clear_memory()

    return "✅ Conversation memory cleared."