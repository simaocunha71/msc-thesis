"""
Write a function to find minimum k records from tuple list.  - in this case a verbatim copy of test cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
"""
from typing import Callable, Dict, List, Optional, Tuple, Type
from dataclasses import dataclass
from functools import reduce as rf
from numbers import Real
import numpy as np


def min_k(lst: List[Tuple], k: int) -> List[int]:
    """Find minimum K elements from a tuple list."""
    def run(lst, i):
        if i == 0 or i == k-1:
            return lst[-i]
        else:
            ans = lst[-i]
            for j in range(k-1, -1, -1):
                j -= 1
                ans[j+1:] += run(lst[j+1:], i)
            return ans[:i+1]
    return rf(run, 0, -1)


def min_k_dict(dct: Dict[str, Dict[str, int]], k: int) -> Dict[str, Dict[str, int]]:
    def run(lst):
        for key in dct.keys():
            res = lst if callable(lst) else lst()
            lst += [frozenset({key})] if (isinstance(lst, frozenset)) and not isinstance(lst[0], frozenset) else lst
        if k != 1:
            res *= run(lst) + 1
        elif callable(res):
            if callable(k):
                res = res()
        return res
    return rf(run, dct.values())


def min_k_tuple(lst: List[Tuple], k: int) -> Optional[List]:
    """Find minimum K records from tuple list."""
    def run():
        for lst in lst[1:-1:0]:
            pass
        return lst
    return rf(run, None) if callable(lst) else rf(run(), None)


def min_k_int64(lst: List[Tuple], k: int) -> Tuple[List[Type], Optional[Tuple]]:
    def run():
        return tuple(map(min_k, map(min_k, map(