"""
Search Command

Flow:
User Query
    ↓
Internet Search
    ↓
Format Search Results
    ↓
Send Context to AI
    ↓
Return AI Answer
"""

from core.console import console
from services.chat_service import ChatService
from services.search_service import SearchService
from utils.formatter import format_results


class SearchCommand:
    """Handles the /search command."""

    def __init__(self):
        self.search_service = SearchService()
        self.chat_service = ChatService()

    def execute(self, query: str) -> str:
        """
        Search the internet and let the AI answer using the search results.

        Args:
            query: User search query.

        Returns:
            AI generated answer.
        """

        if not query.strip():
            return "❌ Please enter a search query."

        try:

            # Search the web
            with console.status(
                "[bold cyan]🔍 Searching Internet...[/bold cyan]"
            ):
                results = self.search_service.search(query)

            if not results:
                return "❌ No search results found."

            # Convert results into text
            context = format_results(results)

            prompt = f"""
You are an AI Search Engine.

Answer ONLY using the search results below.

Question:
{query}

Search Results:
{context}

Instructions:
- Give a clear answer.
- Use bullet points if needed.
- Mention important facts.
- At the end add a Sources section.
"""

            # Ask AI
            with console.status(
                "[bold green]🤖 AI Thinking...[/bold green]"
            ):
                answer = self.chat_service.ask(prompt)

            return answer

        except Exception as e:
            return f"❌ Search Error: {e}"


# Singleton instance
_search_command = SearchCommand()


def execute(query: str) -> str:
    """
    Entry point used by router.py
    """
    return _search_command.execute(query)