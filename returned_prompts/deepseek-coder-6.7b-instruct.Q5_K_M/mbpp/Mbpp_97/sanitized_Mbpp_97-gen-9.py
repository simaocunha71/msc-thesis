def frequency_lists(lst):
    freq = {}
    for sublist in lst:
        for item in sublist:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
    return freq