def merge_dictionaries_three(dict1, dict2, dict3):
    result = {}
    for d in (dict1, dict2, dict3):
        result.update(d)
    return result
