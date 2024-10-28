def frequency_lists(test_list):
    frequency_dict = {}
    for i in test_list:
        for j in i:
            if j in frequency_dict:
                frequency_dict[j] += 1
            else:
                frequency_dict[j] = 1
    return frequency_dict