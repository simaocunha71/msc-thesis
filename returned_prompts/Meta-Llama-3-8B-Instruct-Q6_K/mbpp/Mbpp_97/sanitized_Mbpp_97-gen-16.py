def frequency_lists(lists):
    frequency_dict = {}
    for lst in lists:
        for element in lst:
            if element in frequency_dict:
                frequency_dict[element] += 1
            else:
                frequency_dict[element] = 1
    return frequency_dict