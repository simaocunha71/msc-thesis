def merge_dictionaries_three(dict_one, dict_two, dict_three):
    merged_dict = {}
    for dict in [dict_one, dict_two, dict_three]:
        merged_dict.update(dict)
    return merged_dict
