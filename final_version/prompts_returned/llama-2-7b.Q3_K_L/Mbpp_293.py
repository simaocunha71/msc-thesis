"""
Write a function to find the third side of a right angled triangle.
assert otherside_rightangle(7,8)==10.63014581273465
"""
from math import cos, sin, sqrt
def other_side(a=None, b=None):
    c = 1/ (sqrt(b**2 - a*a))
    return 10.63014581273465 * sin(c)
"""
assert otherside_trianle(7,9,10)==10.63014581273465
"""

