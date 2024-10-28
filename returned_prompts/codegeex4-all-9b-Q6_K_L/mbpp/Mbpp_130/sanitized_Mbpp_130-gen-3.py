def max_occurrences(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    max_frequency = max(frequency.values())
    for item, count in frequency.items():
        if count == max_frequency:
            return item