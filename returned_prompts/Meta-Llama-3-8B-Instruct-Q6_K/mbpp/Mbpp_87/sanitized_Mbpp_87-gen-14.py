def merge_dictionaries_three(dict1, dict2, dict3):
    merged = dict1.copy()
    merged.update(dict2)
    merged.update(dict3)
    return merged