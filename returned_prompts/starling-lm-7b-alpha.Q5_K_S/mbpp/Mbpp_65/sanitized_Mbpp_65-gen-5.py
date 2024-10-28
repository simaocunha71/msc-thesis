def recursive_list_sum(input_list):
    flattened = [item for sublist in input_list for item in sublist]
    return sum(flattened)