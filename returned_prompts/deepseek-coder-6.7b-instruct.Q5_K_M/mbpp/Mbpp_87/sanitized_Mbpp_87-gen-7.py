def merge_dictionaries_three(dict1, dict2, dict3):
    merged = {**dict1, **dict2, **dict3}
    return merged
dict1 = { "R": "Red", "B": "Black", "P": "Pink" }
dict2 = { "G": "Green", "W": "White" }
dict3 = { "O": "Orange", "W": "White", "B": "Black" }