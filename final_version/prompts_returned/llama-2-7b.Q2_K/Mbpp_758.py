"""
Write a function to count lists within a list. The function should return a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurencies in the original list.
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
"""

def unique_sublists(list_of_lists):
    """Count occurrence of tuples in the original list.
    :type list_of_lists: List[List[int]]
    :rtype: Dictionary[Tuple[int, int], int]
    """
    return dict([(i, len(set(map(str, s))))) for i,(s) in enumerate(list_of_lists)]