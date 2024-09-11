def recursive_list_sum(input_list):
    flattened = [item for sublist in input_list for item in sublist]
    return sum(flattened)

# Test
assert recursive_list_sum([1, 2, [3,4],[5,6]]) == 21

# Recursive function to flatten a list
def recursive_list_flatten(input_list):
    flattened = []
    for item in input_list:
        if isinstance(item, list):
            flattened += recursive_list_flatten(item)
        else:
            flattened.append(item)
    return flattened

# Test
assert recursive_list_flatten([1, 2, [3,4],[5,6]]) == [1, 2, 3, 4, 5, 6]

# Recursive function to sum all of the elements in a list
def recursive_list_sum(input_list):
    flattened = recursive_list_flatten(input_list)
    return sum(flattened)

# Test
assert recursive_list_sum([1, 2, [3,4],[5,6]]) == 21

# Recursive function to find the maximum of all of the elements in a list
def recursive_list_max(input_list):
    flattened = recursive_list_flatten(input_list)
    return max(flattened)

# Test
assert recursive_list_max([1, 2, [3,4],[5,6]]) == 6

# Recursive function to find the minimum of all of the elements in a list
def recursive_list_min(input_list):
    flattened = recursive_list_flatten(input_list)
    return min(flattened)

# Test
assert recursive_list_min([1, 2, [3,4],[5,6]]) == 1

# Recursive function to check if all of the elements in a list are the same
def recursive_list_all_same(input_list):