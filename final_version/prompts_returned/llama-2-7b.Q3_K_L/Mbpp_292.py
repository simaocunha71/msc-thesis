"""
Write a python function to find quotient of two numbers (rounded down to the nearest integer).
assert find(10,3) == 3
"""

def find(x,y):
    quotient = (x % y) // y
    return int((quotient + y) // y) if x > 0 else int((quotient - y) // y)