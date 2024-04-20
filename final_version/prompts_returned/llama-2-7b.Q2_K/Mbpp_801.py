"""
Write a python function to count the number of equal numbers from three given integers.
assert test_three_equal(1,1,1) == 3
"""

def test_three_equal(a,b,c):
    if not ((a*b)*(c-1)) <= (a-1):
        return False
    return True
