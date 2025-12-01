import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
class Config():
    RAPID_API_HOST = os.getenv(
        'RAPID_API_HOST', 'kanjialive-api.p.rapidapi.com')
    RAPID_API_KEY =  os.getenv('RAPID_API_KEY')
    