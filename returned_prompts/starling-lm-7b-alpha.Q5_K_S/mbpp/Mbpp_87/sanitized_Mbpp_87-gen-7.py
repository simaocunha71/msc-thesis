def merge_dictionaries_three(dict1, dict2, dict3):
    new_dict = dict1.copy()
    new_dict.update(dict2)
    new_dict.update(dict3)
    return new_dict