import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        request_response = requests.get(self.url)
        return request_response.content

    def load_json(self):
        return json.loads(self.get_response_body())