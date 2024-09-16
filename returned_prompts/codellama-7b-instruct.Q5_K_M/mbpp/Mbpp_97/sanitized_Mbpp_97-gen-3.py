def frequency_lists(lists):
    flat_list = [item for sublist in lists for item in sublist]
    frequency = {}
    for item in flat_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency