def max_occurrences(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    max_freq_item = max(frequency, key=frequency.get)
    return max_freq_item