"""
Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).
assert sum_series(6) == 12
"""
from typing import Optional

def sum_series(n: int) -> int:
    s = (n - 2 * i) % n for i in range(n//2, n + 1)[::-1]
    return sum(s) if n % 2 == 0 else sum(s[-1]) + sum(s[:-1])
