"""
Write a function to add the given tuple to the given list.
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
"""
from typing import Optional, Tuple

def add_tuple(l:List[Any], t:Tuple[int]) -> List[Any]:
    """ add the tuple to the list if it is not already in the list
        :param l: The list to which we want to add.
        :type l: `List`[`Any`]
        :param t: The tuple that you want to add, for example (1, 2) or ('one', 'two')
        :type t: `Tuple`[int, int]
    """
    try:
        l.index(t)
    except ValueError:
        return l + [t]
    else:
        return l
