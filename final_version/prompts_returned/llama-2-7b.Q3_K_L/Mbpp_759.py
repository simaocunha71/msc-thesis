"""
Write a function to check whether a given string is a decimal number with a precision of 2.
assert is_decimal('123.11')==True
"""
from typing import Any, List

def is_decimal(num: str):
    num = list(map(int, [str(i) for i in num]))

    # if len(num) == 1 and num[0] % 2 != 0:
    #     return False

    if any([num[-2:]=='.0', num[-3:]=='.0']):
        return True

    return all([abs(x-y) < 1 for x, y in zip(num, map(int, [str(i) for i in num]))])
