from rich.console import Console

from core.ui import show_banner, show_answer, show_error
from router import Router

console = Console()
router = Router()

show_banner()

while True:

    try:

        user = input("\n[You] ")

        answer = router.route(user)

        if answer is None:
            continue

        if user.startswith("/chat") or user.startswith("/search"):
            show_answer(answer)
        else:
            console.print(answer)

    except SystemExit:

        console.print("\n👋 Goodbye!")
        break

    except Exception as e:

        show_error(str(e))