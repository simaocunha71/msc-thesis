def frequency_lists(lst):
    freq = {}
    for sublist in lst:
        for item in sublist:
            freq[item] = freq.get(item, 0) + 1
    return freq