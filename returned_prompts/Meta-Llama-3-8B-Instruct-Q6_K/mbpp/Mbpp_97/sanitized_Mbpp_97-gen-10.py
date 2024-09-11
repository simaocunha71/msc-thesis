def frequency_lists(list_of_lists):
    freq_dict = {}
    for sublist in list_of_lists:
        for item in sublist:
            if item in freq_dict:
                freq_dict[item] += 1
            else:
                freq_dict[item] = 1
    return freq_dict