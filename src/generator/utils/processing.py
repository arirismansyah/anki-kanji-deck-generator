import pandas as pd
import re
from helper.classes import GradeLevel, JLPTLevel, GRADE_TO_JLPT_MAP, JLPT_TO_GRADE_MAP
class Preprocessing:
    def filter_kanji_list(self, kanji_list:list, key:str, value)-> list:
        result = []
        
        if key=='grade' and (value==None or pd.isna(value)):
            for item in kanji_list:
                item_value = item.get(key)
                if (item_value == None or pd.isna(item_value)):
                    result.append(item)

        for item in kanji_list:
            item_value = item.get(key)

            if isinstance(value, (list, tuple, set)):
                if item_value in value:
                    result.append(item)

            elif isinstance(value, re.Pattern):
                if isinstance(item_value, str) and value.search(item_value):
                    result.append(item)

            elif callable(value):
                if value(item_value):
                    result.append(item)

            else:
                if item_value == value:
                    result.append(item)

        return result
    
    def extract_nested(self, data, path):
        """
        Extract nested JSON menggunakan dot notation atau list.
        Auto handle list: ambil elemen pertama.
        """

        # convert 'a.b.c' → ['a','b','c']
        if isinstance(path, str):
            keys = path.split(".")
        else:
            keys = path

        current = data

        for key in keys:
            if isinstance(current, list):
                if not current:
                    return None
                current = current

        

            current = current[key]

        # final unwrap list
        if isinstance(current, list):
            return current if current else None

        return current


    def extract_values(self, data: dict, keys: dict):
        """
        
        """
        result = {}

        for key in keys.keys():
            try:
                value = self.extract_nested(data, key)
                result[keys[key]] = value
            except Exception as e:
                result[keys[key]] = None

        return result
    
    def grade_to_jlpt(self, grade: int | GradeLevel) -> JLPTLevel:
        """Convert elementary school grade → JLPT level."""

        if isinstance(grade, int):
            try:
                grade = GradeLevel(grade)
            except ValueError:
                return JLPTLevel.N1

        return GRADE_TO_JLPT_MAP.get(grade, JLPTLevel.N1)
    
    def jlpt_to_grade(self, jlpt: str | JLPTLevel) -> list[GradeLevel]:
        """Convert JLPT level → possible Grade levels."""

        if isinstance(jlpt, str):
            try:
                jlpt = JLPTLevel(jlpt.lower())
            except ValueError:
                raise ValueError(f"Invalid JLPT level: {jlpt}")

        return JLPT_TO_GRADE_MAP[jlpt]
