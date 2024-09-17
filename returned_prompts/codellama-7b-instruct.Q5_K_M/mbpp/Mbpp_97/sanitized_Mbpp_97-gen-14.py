def frequency_lists(list_of_lists):
    flat_list = [item for sublist in list_of_lists for item in sublist]
    frequency = {}
    for i in flat_list:
        frequency[i] = flat_list.count(i)
    return frequency