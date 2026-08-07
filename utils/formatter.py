def format_results(results):

    text = ""

    for index, item in enumerate(results, start=1):

        title = item.get("title", "")
        body = item.get("body", "")
        href = item.get("href", "")

        text += (
            f"{index}. {title}\n"
            f"{body}\n"
            f"Source: {href}\n\n"
        )

    return text