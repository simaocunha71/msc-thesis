def frequency_lists(l):
    freq = {}
    for sublist in l:
        for item in sublist:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
    return freq