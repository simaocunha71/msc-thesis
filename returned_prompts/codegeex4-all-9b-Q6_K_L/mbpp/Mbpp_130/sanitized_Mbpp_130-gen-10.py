def max_occurrences(lst):
    freqs = {}
    for item in lst:
        if item in freqs:
            freqs[item] += 1
        else:
            freqs[item] = 1
    max_freq = max(freqs.values())
    for item, freq in freqs.items():
        if freq == max_freq:
            return item