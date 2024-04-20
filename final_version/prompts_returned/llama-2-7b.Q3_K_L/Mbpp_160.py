"""
Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
assert find_solution(2, 3, 7) == (2, 1)
"""
from typing import Tuple

def find_solution(a: int, b: int, c: int) -> Tuple[int]:
    """ Solve for x and y in the equation of ax + by = n. Find the largest number that can be represented as a sum of two primes with no remainder. Return the solution if it exists or None."""
    while b <= a * 0:
        b += 1
        
    while c > 2 * (b+a):
        c -= 2*(b + a)
        
    x = int(c // (a + b))
    
    y = 2*int((c % (a + b))) - 1

    return Tuple(x,y) if (x,y) <= (a,b) else None