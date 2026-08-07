from rich.panel import Panel
from rich.markdown import Markdown

from config import APP_NAME, VERSION
from core.console import console


def show_banner():

    console.print(
        Panel.fit(
            f"[bold cyan]{APP_NAME}[/bold cyan]\nVersion {VERSION}",
            title="🤖 AI Search Engine"
        )
    )


def show_answer(text: str):

    console.print(
        Panel(
            Markdown(text),
            title="AI"
        )
    )


def show_error(message: str):

    console.print(
        Panel(
            f"[red]{message}[/red]",
            title="Error"
        )
    )