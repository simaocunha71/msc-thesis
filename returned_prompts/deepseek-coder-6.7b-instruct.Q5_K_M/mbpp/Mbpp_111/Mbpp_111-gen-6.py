"""
We will use list comprehension to solve this problem. We will iterate over the first list in the nested list, and check if each element of the first list is also in the other lists. If it is, we will add it to our result list.
"""

def common_in_nested_lists(nested_lists):
    return [item for item in nested_lists[0] if all(item in sublist for sublist in nested_lists)]
"""
Note: The time complexity of this function is O(n^2), because for each element in the first list, we are checking if it is in all the other lists. This means that if the first list is very long, this function could take a long time to finish. If you have a large number of lists and each of them is very long, you might want to look into a different approach.
"""

print(set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))) # should print {18, 12}

# Alternative approach
"""
We can use Python's built-in set data structure to solve this problem in a more efficient way. We can convert each sublist into a set and then use the intersection method to find the common elements.
"""

def common_in_nested_lists(nested_lists):
    return set(nested_lists[0]).intersection(*[set(sublist) for sublist in nested_lists])
"""
This approach has a time complexity of O(n), because we are converting each sublist into a set and finding the intersection. This means that it will be much faster than the previous approach, especially for large lists.
"""

print(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])) # should