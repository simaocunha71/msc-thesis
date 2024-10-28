def frequency_lists(lst):
    freq = {}
    for sublist in lst:
        for element in sublist:
            if element in freq:
                freq[element] += 1
            else:
                freq[element] = 1
    return freq