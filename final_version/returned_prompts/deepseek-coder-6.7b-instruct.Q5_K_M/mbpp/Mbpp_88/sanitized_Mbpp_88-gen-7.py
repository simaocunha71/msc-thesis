def freq_count(lst):
    freqs = {}
    for num in lst:
        if num in freqs:
            freqs[num] += 1
        else:
            freqs[num] = 1
    return freqs