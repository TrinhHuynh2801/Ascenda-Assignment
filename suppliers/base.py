import requests

class BaseSupplier:
    @staticmethod
    def endpoint():
        """URL to fetch supplier data"""

    @staticmethod
    def parse(obj: dict):
        """Parse supplier-provided data into Hotel object"""

    def fetch(self):
        url = self.endpoint()
        resp = requests.get(url)
        return [self.parse(dto) for dto in resp.json()]
