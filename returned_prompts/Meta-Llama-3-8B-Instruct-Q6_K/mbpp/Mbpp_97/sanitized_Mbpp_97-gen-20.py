def frequency_lists(lists):
    frequency_dict = {}
    for lst in lists:
        for num in lst:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
    return frequency_dict