"""
To find the common elements in the given nested lists, we can use a for loop to iterate through each list and use an if statement to check if the current element is present in all lists. If it is, we can add it to a new list that stores the common elements.

Here is a function that implements this logic:

def common_in_nested_lists(lists):
    common = []
    for list in lists:
        for item in list:
            if all(item in sublist for sublist in lists):
                common.append(item)
    return common
"""

def common_in_nested_lists(lists):
    common = []
    for list in lists:
        for item in list:
            if all(item in sublist for sublist in lists):
                common.append(item)
    return common

# Test the function
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])

# Test with a different example
assert set(common_in_nested_lists([[1, 2, 3], [3, 4, 5], [4, 5, 6]]))==set([3, 4, 5])

# Test with an empty input
assert set(common_in_nested_lists([]))==set([])

# Test with a single list input
assert set(common_in_nested_lists([[1, 2, 3]]))==set([1, 2, 3])

print("All tests passed.")



























































































