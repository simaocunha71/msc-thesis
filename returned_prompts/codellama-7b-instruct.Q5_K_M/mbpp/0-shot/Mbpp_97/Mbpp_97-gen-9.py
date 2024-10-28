"""
def frequency_lists(lists):
    flattened_list = [item for sublist in lists for item in sublist]
    frequency_dict = {}
    for element in flattened_list:
        if element not in frequency_dict:
            frequency_dict[element] = 1
        else:
            frequency_dict[element] += 1
    return frequency_dict
"""
