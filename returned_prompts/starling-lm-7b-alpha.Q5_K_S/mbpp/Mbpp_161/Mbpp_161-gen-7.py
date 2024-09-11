"""
def remove_elements(list1, list2):
    for i in list2:
        list1.remove(i)
    return list1
"""

# Using list comprehension to remove elements:
def remove_elements(list1, list2):
    return [i for i in list1 if i not in list2]

# Testing the function:
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]

# Removing multiple elements from a list:
assert remove_elements([1, 1, 2, 3, 4, 4, 5, 6, 6], [1, 2, 3, 4, 5]) == [6]

# Removing all elements from a list:
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == []

# Removing no elements from a list:
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Removing elements from an empty list:
assert remove_elements([], [1, 2, 3, 4, 5]) == []

# Removing elements from a list with only one element:
assert remove_elements([1], [1]) == []

# Removing elements from a list with only one element (case 2):
assert remove_elements([1], []) == [1]

# Removing elements from a list with only one element (case 3):
assert remove_elements([], [1])