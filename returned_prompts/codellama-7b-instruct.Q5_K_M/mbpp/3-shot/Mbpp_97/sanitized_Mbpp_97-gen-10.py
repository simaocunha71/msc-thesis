def frequency_lists(lst_of_lists):
    flattened_list = [item for sublist in lst_of_lists for item in sublist]
    frequency_dict = {}
    for element in flattened_list:
        frequency_dict[element] = frequency_dict.get(element, 0) + 1
    return frequency_dict