"""
Write a python function to find the sum of all odd natural numbers within the range l and r.
assert sum_in_range(2,5) == 8
"""
from typing import Optional

def sum_in_range(l: int = 0, r: int = None) -> int:
    """
    :type l: int
    :rtype: int
    """
    if not isinstance(r, Optional):
        return (r - l + 1).sum()
    elif isinstance(r, int) and r > 0:
        return (l + r).sum()

print("Given range is {l} to {r}, sum will be = {sum_in_range}".format(
        l=l, r=r, sum_in_range=sum_in_range(l, r)))