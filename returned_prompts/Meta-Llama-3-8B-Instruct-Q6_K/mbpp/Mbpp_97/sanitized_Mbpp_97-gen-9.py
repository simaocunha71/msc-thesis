def frequency_lists(lists):
    flattened = [item for sublist in lists for item in sublist]
    frequency = {}
    for item in flattened:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency