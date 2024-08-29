"""
A decagonal number is given by the formula:

    D_n = n * (7*n - 5)/2

We can use this formula to find the nth decagonal number.

Here is a Python function that does this:
"""

def is_num_decagonal(n):
    return n * (7*n - 5)//2

print(is_num_decagonal(3))  # 27


