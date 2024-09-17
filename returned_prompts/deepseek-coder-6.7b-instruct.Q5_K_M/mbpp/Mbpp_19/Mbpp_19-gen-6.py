
def test_duplicate(lst):
    if len(lst) == len(set(lst)):
        return False
    else:
        return True
"""
This function works by converting the list to a set. A set is an unordered collection of unique elements, so if there are any duplicate elements in the list, the length of the set will be smaller than the length of the list. If the lengths are the same, there were no duplicate elements in the list.
"""

