"""
Write a python function to return the negative numbers in a list.
assert neg_nos([-1,4,5,-6]) == [-1,-6]
"""
from typing import Any

def neg_nos(x: Any) -> int:  # type: ignore
    """Returns true if x is negative
       https://www.geeksforgeeks.org/write-function-to-return-negative-numbers-in-a-list-2130748519.html#:~:text=Write%20a%20python%20function%2D%20neg_nos(x)%20-%20%40geeksforgeeks to,to%20return%20negative%20numbers%20in%20a%20list
    """
    if x is None: return -1
    if type(x).__name__ == "int":  # type: ignore
        if not (x < 0): return -1
        else: return x
    elif type(x).__name__ == "float":  # type: ignore
        if str(int(x)) == "-inf" or str(int(x)).startswith('-'):
            return int(x)
        else:
            return -1
    
if __name__ == '__main__':
    neg_nos(-1,5,-6)-3
