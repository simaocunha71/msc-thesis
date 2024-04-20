"""
Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
"""
from typing import Any, Dict, List, Optional, Tuple
def merge_two_lists(lists: List[List[Any]]) -> List[Tuple]:
    """Returns the lists with the first element of each list and the second one.
    Args:
        lists (list of lists): a single-dimension array, where each sublist has two elements.
    Returns:
        tuples ([(el1, el2)]): where each tuple contains the first two elements of each sublist in the input list of lists.
    """
    out_lists = []
    for sublist in lists:
        new_sublist = [sublist[0], sublist[1]]
        out_lists.append(new_sublist)
    return out_lists

if __name__=="__main__":
  print("Hello, world!")