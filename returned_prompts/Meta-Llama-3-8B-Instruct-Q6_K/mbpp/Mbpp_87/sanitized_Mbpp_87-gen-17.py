def merge_dictionaries_three(dict1, dict2, dict3):
    merged_dict = {}
    for key in dict1:
        if key not in merged_dict:
            merged_dict[key] = dict1[key]
    for key in dict2:
        if key not in merged_dict:
            merged_dict[key] = dict2[key]
    for key in dict3:
        if key not in merged_dict:
            merged_dict[key] = dict3[key]
    return merged_dict