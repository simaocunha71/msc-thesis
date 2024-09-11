"""
To solve this problem we can use a set to store the unique elements.
Then we can iterate through each nested list and add the elements to the set.
Finally, we can return the set.
"""

def common_in_nested_lists(lists):
    set_ = set()
    for l in lists:
        for i in l:
            set_.add(i)
    return set_
# common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])
"""
"""

# Common Elements in Nested Lists
# Given a list of lists of integers, write a function to find all the common elements in them.

def common_in_nested_lists(lists):
    """
    lists: a list of lists of integers
    return a set of integers
    """
    set_ = set()
    for l in lists:
        for i in l:
            set_.add(i)
    return set_

# Test Cases
print(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))  # {18, 12}
print(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]]))  # {3, 2, 1}
print(common_in_nested_lists([[1], [2, 3], [4, 5, 6], [7, 8, 9]]))  # {1}
print(common_in_nested_lists([[1, 2, 3], [4, 5], [6, 7, 8], [9, 10, 11]])) 