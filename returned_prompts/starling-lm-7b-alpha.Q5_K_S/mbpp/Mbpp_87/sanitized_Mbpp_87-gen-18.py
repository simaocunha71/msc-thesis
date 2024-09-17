def merge_dictionaries_three(dict1: dict, dict2: dict, dict3: dict) -> dict:
    result = dict1.copy()
    result.update(dict2)
    result.update(dict3)
    return result