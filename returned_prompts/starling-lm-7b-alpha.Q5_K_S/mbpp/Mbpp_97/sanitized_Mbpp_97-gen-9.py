def frequency_lists(lst):
    freq = {}
    for el in lst:
        if el in freq:
            freq[el] += 1
        else:
            freq[el] = 1
    return freq