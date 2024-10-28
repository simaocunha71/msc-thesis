def freq_count(lst):
    freq = {}
    for element in lst:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1
    return freq