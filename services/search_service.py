from providers.search_provider import SearchProvider


class SearchService:

    def __init__(self):

        self.provider = SearchProvider()

    def search(self, query: str):

        return self.provider.search(query)