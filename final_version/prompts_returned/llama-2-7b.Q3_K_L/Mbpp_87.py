"""
Write a function to merge three dictionaries into a single dictionary.
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
"""
from typing import List, Dict

def merge_dictionaries(dict1: dict, dictionary2: dict, dictionary3: dict) -> List[Dict]:
    """ Merge the three dictionaries.
        :param dict1: Dictionary 1
        :type dict1: dict
        :param dictionary2: Dictionary 2
        :type dictionary2: dict
        :return: Merged Dicts as a list"""
    
    merged_dict = []
    for key,value in dict(dict1).items():
        if value not in dict(dictionary2) and value not in dict(dictionary3):
            merged_dict.append({key: value})
        
    return sorted(merged_dict, key=lambda x:x[0])
