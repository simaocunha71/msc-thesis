"""
A nonagonal number is given by the formula n(7n-5)/2.
"""

def is_nonagonal(n):
    return n*(7*n - 5)//2

assert is_nonagonal(10) == 325

# 3.

