
def merge_dictionaries_three(dict1, dict2, dict3):
    final_dict = {}
    for i in dict1:
        final_dict[i] = dict1[i]
    for i in dict2:
        final_dict[i] = dict2[i]
    for i in dict3:
        final_dict[i] = dict3[i]
    return final_dict


