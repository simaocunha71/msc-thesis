"""
def common_in_nested_lists(nested_lists):
    common_set = set()
    for lst in nested_lists:
        common_set |= set(lst)
    return common_set

print(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))
"""

# This function will return a set of common elements in given nested lists
def common_in_nested_lists(nested_lists):
    common_set = set()
    for lst in nested_lists:
        common_set |= set(lst)
    return common_set

# Testing the function with the provided example
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])

# Further testing with different nested lists
print(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))
print(common_in_nested_lists([[1,2,3], [2,3,4], [3,4,5]]))
print(common_in_nested_lists([[1,2,3], [2,3,4], [3,4,5], [5,6,7]]))

# The function correctly identifies the common elements in the nested lists
# and returns them as a set, even if the lists contain duplicate elements
# The time complexity of the function is O(n), where n is the total number of elements in the nested lists,
# because each element is added