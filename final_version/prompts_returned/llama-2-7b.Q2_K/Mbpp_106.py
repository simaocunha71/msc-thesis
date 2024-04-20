"""
Write a function to append the given list to the given tuples.
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
"""
from typing import Optional, Tuple

def add_lists(
        listToAdd: Optional[List[int]], tuples: Tuple[Tuple]) -> Tuple:
    """ Append the given list to the given tuples.
    :param listToAdd: The List to append into each tuple in the array
    :type listToAdd: list
    :param tuples: The tuples to append the list into.
    :type tuples: (List,...)
    """
    if not isinstance(listToAdd, list):
        raise TypeError("Expecting a list as argument.")
    result = []
    for i in range(0, len(tuples)):
        # append the given list to each tuple
        tmp = tuples[i] + [listToAdd[-1]]
        result.append(tuple(tmp))  # we use a list of tuples instead of just a tuple
    return tuple([result])