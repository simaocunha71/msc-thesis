def frequency_lists(lst):
    flattened_list = [item for sublist in lst for item in sublist]
    frequency_dict = {}
    for item in flattened_list:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1
    return frequency_dict