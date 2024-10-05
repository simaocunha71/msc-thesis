    # Create a mapping from node value to its index
    mapping = {}
    for idx, elem in enumerate(arr):
        if elem % 2 == 0:
            mapping[elem] = idx

    # Find the smallest even value
    smallest_value = min(mapping.keys())

    # If multiple smallest values, choose the one with smallest index
    if mapping[smallest_value] != min(mapping[key] for key in mapping.keys()):
        smallest_value = min(mapping[key] for key in mapping.keys())

    return [smallest_value, smallest_value]


