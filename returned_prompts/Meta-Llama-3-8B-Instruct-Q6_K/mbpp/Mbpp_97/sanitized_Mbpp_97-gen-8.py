def frequency_lists(lists):
    frequency = {}
    for lst in lists:
        for element in lst:
            if element in frequency:
                frequency[element] += 1
            else:
                frequency[element] = 1
    return frequency