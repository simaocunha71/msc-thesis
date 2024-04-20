"""
Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
assert is_polite(7) == 11
"""
from typing import Optional, List

def is_polite(N: int)->int:
    """
    A number is polite iff it's the sum of its divisors.
    
    >>> n = 3528
    >>> sum(i*j for i in range(1, n) for j in (n-i+1)) == n
    True
    """
    result = False
    if N > 0:
        for m in range(1, int(N//2)+1):
            div = [i*j for i in range(m, int(N/m)+1) for j in (N-i+1)]
            if sum(div) == N:
                result = True
    return result