def merge_dictionaries_three(dict1, dict2, dict3):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = value
    for key, value in dict3.items():
        if key in result:
            if result[key] != value:
                raise ValueError(f"Key {key} has different values in dictionaries")
        else:
            result[key] = value
    return result