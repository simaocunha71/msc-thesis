def frequency_lists(lst):
    flattened_list = [num for sublist in lst for num in sublist]
    frequency_dict = {}
    for num in flattened_list:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    return frequency_dict

