def frequency_lists(lst):
    freq = {}
    for i in lst:
        for j in i:
            if j not in freq:
                freq[j] = 1
            else:
                freq[j] += 1
    return freq