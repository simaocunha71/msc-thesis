def extract_singly(input):
    # flatten the list of lists
    flatten_list = [num for sublist in input for num in sublist]
    # convert the flattened list to set
    flat_set = set(flatten_list)
    # return the set
    return flat_set