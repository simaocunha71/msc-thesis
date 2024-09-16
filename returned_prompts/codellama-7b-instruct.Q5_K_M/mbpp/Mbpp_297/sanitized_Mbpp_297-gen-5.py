def flatten_list(l):
    # initialize an empty list to store the flattened list
    flattened_list = []

    # iterate through the nested list
    for element in l:
        # if the element is a list, then recursively call the flatten_list function
        if type(element) == list:
            flattened_list.extend(flatten_list(element))
        else:
            flattened_list.append(element)

    return flattened_list