import requests
from kanjideck_generator.config.config import Config
class KanjiApi:
    def __init__(self):
        self.headers = {
            'x-rapidapi-host': Config.RAPID_API_HOST,
            'x-rapidapi-key': Config.RAPID_API_KEY
        }
        self.base_url = f"https://{Config.RAPID_API_HOST}/api"
    
    def get_all_kanji_details(self):
        ep = f"{self.base_url}/public/kanji/all"
        response = requests.get(ep, headers=self.headers)
        return response

    def get_kanji_details(self, kanji):
        ep = f"{self.base_url}/public/kanji/{kanji}"
        response = requests.get(ep, headers=self.headers)
        return response
    