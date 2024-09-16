def frequency_lists(lists):
    # convert list of lists to set of elements
    elements = set(sum(lists, []))
    # initialize frequency dictionary
    frequency = {element: 0 for element in elements}
    # loop through each list and update frequency dictionary
    for lst in lists:
        for element in lst:
            frequency[element] += 1
    # return frequency dictionary
    return frequency