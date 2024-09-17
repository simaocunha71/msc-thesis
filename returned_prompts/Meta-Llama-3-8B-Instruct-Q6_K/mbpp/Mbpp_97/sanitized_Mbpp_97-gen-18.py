def frequency_lists(lists):
    frequency = {}
    for lst in lists:
        for num in lst:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
    return frequency