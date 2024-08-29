"""
Here is the python code for the problem:

def cal_sum(n):
    # Perrin sequence starts with 3 and 0, 2
    a, b, c = 3, 0, 2
    if n == 0:
        return 0
    if n == 1:
        return a
    if n == 2:
        return b + c
    for _ in range(3, n+1):
        a, b, c = c, a, a+b
    return a

assert cal_sum(9) == 49
"""

