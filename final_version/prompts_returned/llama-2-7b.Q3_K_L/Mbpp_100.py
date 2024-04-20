"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""
from typing import Optional

def next_smallest_palindrome(n: int):
    l = []
    while n > 3:
        r = ((n+1)/2-1)*2
        if n % (r*2) == 0 and n <= r*2:
            return r // 2 + 1
        
        l.append(r//2)
        n -= l[-1]*2
    
    return l[0]