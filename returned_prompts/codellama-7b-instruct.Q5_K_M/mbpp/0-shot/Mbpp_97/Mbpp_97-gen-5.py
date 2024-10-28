"""
def frequency_lists(list_of_lists):
    list_flattened = [item for sublist in list_of_lists for item in sublist]
    frequency_dict = {}
    for element in list_flattened:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    return frequency_dict
"""
