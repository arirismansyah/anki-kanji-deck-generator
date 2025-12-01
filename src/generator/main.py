
import os
import random
from utils.api import KanjiApi
from utils.processing import Preprocessing
from helper.classes import LevelType
import genanki
import pandas as pd

class KanjiDeck(KanjiApi, Preprocessing):
    def __init__(self):
        super().__init__()
        self.data_keys = {
            'kanji.character': 'kanji',
            'meaning': 'meaning',
            'kunyomi_ja': 'kunyomi_ja',
            'kunyomi': 'kunyomi',
            'onyomi_ja': 'onyomi_ja',
            'onyomi': 'onyomi',
            'mn_hint': 'mnemonic',
        }
        
        self.front_html = self.load_template('../template/front.html')
        self.back_html = self.load_template('../template/back.html')
        self.styling_css = self.load_template('../template/styling.css')
        self.result_dir = '../result'
    
    def generate_deck_data(self, level_type:LevelType, level, keys:dict):
        if level_type == LevelType.JLPT:
            grades = self.jlpt_to_grade(level)
        else:
            grades = [level]
        
        
            
        if isinstance(grades, list):
            if len(grades)>0:
                for grade in grades:
                    response = self.get_all_kanji_details()
                    if response.status_code==200:
                        kanji = response.json()
                        if isinstance(kanji, list):
                            filtered_kanji = self.filter_kanji_list(kanji_list=kanji, key='grade', value=grade)
                            if isinstance(filtered_kanji, list) and len(filtered_kanji)>0:
                                list_extracted_kanji = []
                                for kanji in filtered_kanji:
                                    extracted_kanji = self.extract_values(data=kanji, keys=keys)
                                    list_extracted_kanji.append(extracted_kanji)                   
            else:
                response = self.get_all_kanji_details()
                if response.status_code == 200:
                    kanji = response.json()
                    if isinstance(kanji, list):
                        filtered_kanji = self.filter_kanji_list(
                            kanji_list=kanji, key='grade', value=None)
                        if isinstance(filtered_kanji, list) and len(filtered_kanji) > 0:
                            list_extracted_kanji = []
                            for kanji in filtered_kanji:
                                extracted_kanji = self.extract_values(
                                    data=kanji, keys=keys)
                                list_extracted_kanji.append(
                                    extracted_kanji)
                
        return list_extracted_kanji
                                    
    def load_template(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()

    def generate_deck(self, output_filename: str, level_type: LevelType, level: str,):
        MODEL_ID = random.randint(1000000000, 9999999999)  
        DECK_ID = random.randint(1000000000, 9999999999)
        
        model_fileds = []
        data_deck = self.generate_deck_data(level_type=level_type, level=level, keys=self.data_keys)
        
        for field in self.data_keys.values():
            model_fileds.append({'name':field})

        kanji_model = genanki.Model(
            MODEL_ID,
            'Kanji Model Enhanced',
            fields=model_fileds,
            templates=[
                {
                    'name': 'Kanji Card',
                    'qfmt': self.front_html,  # Load dari file
                    'afmt': self.back_html,   # Load dari file
                },
            ],
            css=self.styling_css  # Load dari file
        )

        # Create deck
        kanji_deck = genanki.Deck(
            DECK_ID,
            f'Kanji Deck - {str(level_type).capitalize()} - {str(level).capitalize()}'
        )

        # Tambahkan notes dari data
        for data in data_deck:
            data_fields = []
            for field in self.data_keys.values():
                data_fields.append(data.get(field, ''))
            note = genanki.Note(
                model=kanji_model,
                fields=data_fields
            )
            kanji_deck.add_note(note)

        # Export ke file .apkg
        if not os.path.isdir(self.result_dir):
            os.makedirs(self.result_dir)
            
        output_file = os.path.join(self.result_dir, output_filename)
        genanki.Package(kanji_deck).write_to_file(output_file)
        print(f"Success Generated Deck {str(level_type).capitalize()} : {str(level).capitalize()} - (Kanji Count: {len(data_deck)}) - Output: {output_file}")


