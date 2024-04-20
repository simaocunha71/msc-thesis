"""
Write a function to create a list of N empty dictionaries.
assert empty_list(5)==[{},{},{},{},{}]
"""
from typing import Callable, Dict, List, Optional, Tuple, Type, Union  # noqa: F401
from warnings import warn  # noqa: F401
import os.path

_dicts = [{} for _ in range(5)]

def empty_list(n: int) -> List[Dict]:
    """Create a list of N empty dictionaries.
    :param n: length of the list
    :return: A list of n empty dictionaries.
    Raises: AssertError if n is not an integer or negative, then None is returned.
    """
    _dicts = [_dicts[:n+1]] * len(list(_dicts))
    assert n >= 0 and type(n) == int, "AssertError: n must be a positive integer"
    return _dicts
