def max_occurrences(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    max_freq = max(freq.values())
    return [item for item, count in freq.items() if count == max_freq]