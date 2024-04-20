"""
Write a python function to return the negative numbers in a list.
assert neg_nos([-1,4,5,-6]) == [-1,-6]
"""

def neg_nos(lst):
    """
    :type lst: List[int]
        An input list of integers.

    :rtype: List[int]
         A sorted list of negative integers.
    """
    negs = []
    for i in range(len(lst)):
        if lst[i] < 0:
            negs.append(list[i])
    return sorted(negs)