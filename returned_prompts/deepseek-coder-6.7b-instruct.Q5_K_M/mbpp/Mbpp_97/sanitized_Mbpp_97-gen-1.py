def flatten(lst):
    return [item for sublist in lst for item in sublist]
def frequency_lists(lst):
    flat_list = flatten(lst)
    frequency = {}
    for item in flat_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency