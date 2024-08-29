def Extract(lst):
    return [sublist[0] for sublist in lst if isinstance(sublist, list)]

print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))  # [1, 3, 6]

"""
Explanation:
This function uses a list comprehension to iterate over each element in the input list. If the element is a sublist (checked with `isinstance(sublist, list)`), it gets the first element (`sublist[0]`) and includes it in the new list. If the element is not a sublist, it is ignored.
"""

# Task 2
