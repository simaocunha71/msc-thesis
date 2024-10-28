def frequency_lists(l):
    freq = {}
    for i in l:
        for j in i:
            if j not in freq:
                freq[j] = 1
            else:
                freq[j] += 1
    return freq