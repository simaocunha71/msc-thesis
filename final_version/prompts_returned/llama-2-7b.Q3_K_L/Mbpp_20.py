"""
Write a function to check if the given number is woodball or not.
assert is_woodall(383) == True
"""
from typing import Any, List

def is_woodall(n: int, target: int = 106):
    """
    If n = target then return False, else return True
    :param n:
    :param target:
    :return:
    """
    if (target - 2) * (target - 1) == n*n:
        return False
    return True