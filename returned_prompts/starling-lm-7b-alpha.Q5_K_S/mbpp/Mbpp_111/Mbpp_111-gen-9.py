"""
def common_in_nested_lists(nested_lists):
    result = set()
    for i in nested_lists:
        result.update(i)
    return result
"""

# Alternative Solution
def common_in_nested_lists(nested_lists):
    return set(item for sublist in nested_lists for item in sublist)


# Testing the function
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
print("All test cases passed.")
```