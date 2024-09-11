"""
def flatten_list(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))
"""

# Here's a more Pythonic way to achieve the same result using list comprehension:

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist if not isinstance(item, list)]

print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))

The code uses list comprehension to iterate over each sublist in the nested_list. For each item in the sublist, it checks if the item is not a list (using the isinstance() function) and if so, it adds the item to the result list. This process is repeated for each sublist until all nested elements have been flattened. The result is a single, flat list that contains all the elements from the original nested_list structure.

# Pythonic way of flattening a list
def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist if not isinstance(item, list)]

# Testing the function
assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]) == [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110,