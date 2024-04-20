"""
Write a python function to count the number of lists in a given number of lists.
assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
"""
from typing import List

def count_lists(list_of_lists: List):
    """
    :param list_of_lists: an iterable of lists. A list will be counted as one element in the list.
    :return: The number of lists in the given input.
    """
    if not isinstance(list_of_lists, list) or len(list_of_lists) < 1:
        return 0
    
    return sum([len(i) for i in list_of_lists])

print("Example:")
print("assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4")
