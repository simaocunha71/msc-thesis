
def merge_dictionaries_three(dict1, dict2, dict3):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    merged_dict.update(dict3)
    return merged_dict


