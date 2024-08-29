def is_Monotonic(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)) or all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

print(is_Monotonic([6, 5, 4, 4]))

# Q2:
"""
Write a Python function to find the intersection of two given arrays. The arrays are the same length.
assert array_intersection([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
"""

# A2:
def array_intersection(lst1, lst2):
    return [value for value in lst1 if value in lst2]

print(array_intersection([1, 2, 3, 4], [3, 4, 5, 6]))

# Q3:
"""
Write a Python function that takes an array and a number as input, and returns the array sorted in descending order up to the number provided.
assert sort_descend([4, 2, 9, 7, 5, 1, 8, 3, 6], 5) == [9, 8, 7, 6, 5]
"""

# A3:
def sort_descend(lst, num):
    return sorted(lst, reverse=True)[:num]

print(sort_descend([4, 2, 9, 7, 5, 1, 8, 3, 6], 5))

# Q4:
"""
Write a Python function that takes a list of strings as input and returns a new list with the strings sorted by the last character of each string.
assert sort_strings(['hello', 'world', 'python', 'is', 'awesome']) == ['is', 'awesome', 'hello', 'world', 'python']
"""

# A4:
def sort_strings(lst):
    return sorted(lst, key=lambda x: x[-1])

print(sort_strings