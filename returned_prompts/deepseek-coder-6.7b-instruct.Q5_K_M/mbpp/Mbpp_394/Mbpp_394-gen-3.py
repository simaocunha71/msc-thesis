def check_distinct(t):
    return len(t) == len(set(t))

print(check_distinct((1, 4, 5, 6, 1, 4)))  # False
"""
Explanation:
The function works by converting the tuple to a set. In Python, a set is an unordered collection of unique elements. If the tuple has any duplicate elements, the set will remove them.
If the length of the set is the same as the length of the tuple, this means that the tuple had no duplicates and the function returns True.
If the length of the set is different than the length of the tuple, this means that the tuple had duplicates and the function returns False.
"""


