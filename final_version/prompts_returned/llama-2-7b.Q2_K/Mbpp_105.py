"""
Write a python function to count true booleans in the given list.
assert count([True,False,True]) == 2
"""
from typing import Callable

def count(list: [Callable[..., float]]) -> float:
    """Count values of type Callable such that (lambda x: not not x) in a given list.

    >>> count([True, False, True]) == 2
     True
    """
    # Counting elements which are not not False.
    return sum(not not l for l in list)
