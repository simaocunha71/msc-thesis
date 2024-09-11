"""
def common_in_nested_lists(nested_lists):
    # Flatten the list
    flat_list = [item for sublist in nested_lists for item in sublist]
    # Return the set of common elements
    return set(flat_list)

# Test the function
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""

common_in_nested_lists = lambda nested_lists: set(item for sublist in nested_lists for item in sublist)

assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])

# Common in two lists
assert set(common_in_nested_lists([[1, 2, 3], [3, 4, 5]]))==set([1, 3])

# Common in three lists
assert set(common_in_nested_lists([[1, 2, 3], [3, 4, 5], [2, 4, 6]]))==set([2, 3, 4])

# Common in a single list
assert set(common_in_nested_lists([1, 2, 3]))==set([1, 2, 3])

# Common in empty list
assert set(common_in_nested_lists([]))==set([])

# Common in a list of empty lists
assert set(common_in_nested_lists([[], []]))==set([])

# Common in two lists of empty lists
assert set(common_in_nested_lists([[], []]))==set([])

# Common in nested lists
assert set(common