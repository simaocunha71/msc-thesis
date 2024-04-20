"""
Write a function to check whether the given number is a perfect square or not. 
assert not is_perfect_square(10)
"""
from typing import Union, Any
import math
def is_perfect_square(n: Union[int, float]) -> bool:
    """Checks if x is an integer and returns whether it's a perfect square. 
       If the input value is not an integer (float), 0 will be returned since only ints can return True in this function."""
    if n == 0 or int(n) == n:
        return bool(int(math.sqrt(x)) * int(math.sqrt(x)))
    
    return False

# Driver code
n = input("Enter a number to test: ")
is_perfect_square(n)