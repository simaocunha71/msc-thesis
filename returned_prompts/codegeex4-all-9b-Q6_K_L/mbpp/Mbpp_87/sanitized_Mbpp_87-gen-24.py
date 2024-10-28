def merge_dictionaries_three(dict1, dict2, dict3):
    result = dict1.copy()
    result.update(dict2)
    result.update(dict3)
    return result