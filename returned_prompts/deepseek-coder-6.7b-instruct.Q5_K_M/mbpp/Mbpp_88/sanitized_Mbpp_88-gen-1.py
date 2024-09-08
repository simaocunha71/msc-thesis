def freq_count(lst):
    freqs = {}
    for i in lst:
        if i in freqs:
            freqs[i] += 1
        else:
            freqs[i] = 1
    return freqs