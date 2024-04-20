"""
Write a python function to find the highest power of 2 that is less than or equal to n.
assert highest_Power_of_2(10) == 8
"""

def highest_power_of_2(n):
    x = None
    while True:
        if not(x is None): return x
        if n in [None, 0]: break
        if n%2 == 1 and n != -1:
            x= int((n-x)//2)
        else:
            x = n
    return n