import requests
from configparser import ConfigParser
import os

class BaseAPI:
    def __init__(self):
        # Get absolute path to config.ini
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(base_dir, 'config', 'config.ini')

        # Load config
        config = ConfigParser()
        config.read(config_path)

        self.base_url = config.get('api', 'base_url')

    def get(self, endpoint, **kwargs):
        return requests.get(f"{self.base_url}{endpoint}", **kwargs)

    def post(self, endpoint, data=None, json=None, **kwargs):
        return requests.post(f"{self.base_url}{endpoint}", data=data, json=json, **kwargs)

    def put(self, endpoint, data=None, json=None, **kwargs):
        return requests.put(f"{self.base_url}{endpoint}", data=data, json=json, **kwargs)

    def delete(self, endpoint, **kwargs):
        return requests.delete(f"{self.base_url}{endpoint}", **kwargs)
