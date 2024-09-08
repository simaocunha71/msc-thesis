def frequency_lists(lst):
    frequency = {}
    for sublist in lst:
        for item in sublist:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1
    return frequency