def merge_dictionaries_three(dict1, dict2, dict3):
    merged = {}
    for d in (dict1, dict2, dict3):
        merged.update(d)
    return merged