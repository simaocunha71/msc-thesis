def frequency_lists(lists):
    freq_dict = {}
    for lst in lists:
        for num in lst:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
    return freq_dict