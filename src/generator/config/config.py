import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
class Config():
    RAPID_API_HOST = os.getenv(
        'RAPID_API_HOST', 'kanjialive-api.p.rapidapi.com')
    RAPID_API_KEY = os.getenv(
        'RAPID_API_KEY', 'c417de260amshf499025b6477a05p1fca09jsna149249de0c9')
    DATA_KEYS = {
        'kanji.character': 'kanji',
        'meaning': 'meaning',
        'kunyomi_ja': 'kunyomi_ja',
        'kunyomi': 'kunyomi',
        'onyomi_ja': 'onyomi_ja',
        'onyomi': 'onyomi',
        'mn_hint': 'mnemonic',
    }
    RESULT_DIR = '../result'
