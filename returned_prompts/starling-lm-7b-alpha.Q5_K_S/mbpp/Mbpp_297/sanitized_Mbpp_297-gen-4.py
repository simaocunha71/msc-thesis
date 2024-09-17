def flatten_list(nested_list):
    # initialize an empty list
    flattened_list = []
    # iterate through each element in the nested list
    for item in nested_list:
        # if the item is a list, recursively call the function
        if type(item) == list:
            flattened_list.extend(flatten_list(item))
        else:
            # otherwise, append the item to the flattened list
            flattened_list.append(item)
    return flattened_list