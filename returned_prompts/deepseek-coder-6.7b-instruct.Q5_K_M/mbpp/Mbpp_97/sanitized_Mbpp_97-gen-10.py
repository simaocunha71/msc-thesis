def frequency_lists(list_of_lists):
    frequency_dict = {}
    for sub_list in list_of_lists:
        for element in sub_list:
            if element in frequency_dict:
                frequency_dict[element] += 1
            else:
                frequency_dict[element] = 1
    return frequency_dict