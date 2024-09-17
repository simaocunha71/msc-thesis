def frequency_lists(lst: list) -> dict:
    freq_dict = {}
    for sublist in lst:
        for num in sublist:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
    return freq_dict