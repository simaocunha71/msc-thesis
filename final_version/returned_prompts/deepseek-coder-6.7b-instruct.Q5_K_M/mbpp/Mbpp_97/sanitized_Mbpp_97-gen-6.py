def frequency_lists(lst):
    flat_list = [item for sublist in lst for item in sublist]
    freq = {}
    for item in flat_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq