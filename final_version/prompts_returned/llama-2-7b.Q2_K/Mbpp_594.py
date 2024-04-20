"""
Write a function to find the difference of the first even and first odd number of a given list.
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""
from typing import Any
def diff_even_odd(lst: [Any] = None) -> float:
    """Return the difference of the first even and odd number."""
    if not lst:
        return 0.0
    
    n = len(lst)
    assert n > 0, 'Empty input.'
    
    # First add one to the length of the list so that we can do n // 2 with even numbers.
    l1 = [x + (n-1) for x in lst]
    even_diff = 0
    odd_diff = 0
    
    for i, j in enumerate(l1):
        if (i % 2 == 0 and j > 0):
            even_diff += j
        else:
            odd_diff -= j + 1
        
    return even_diff - odd_diff