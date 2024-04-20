"""
Write a python function to find the last digit of a given number.
assert last_Digit(123) == 3
"""
from typing import Optional

def last_digit(n: int):
    if not n or n < 0: return None
    result = -1
    while n:
        digit = n % 10
        n //= 10
        if digit != 0: result += 1
    return result
\end{code}