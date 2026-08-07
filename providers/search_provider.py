from ddgs import DDGS


class SearchProvider:

    def search(self, query: str, max_results: int = 5):

        with DDGS() as ddgs:

            return list(
                ddgs.text(
                    query,
                    max_results=max_results
                )
            )