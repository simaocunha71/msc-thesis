def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

# Test
print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))
# Output: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]






















"""

def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

# Test
print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))
# Output: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

"""


"""

def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return