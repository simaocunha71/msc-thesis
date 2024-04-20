"""
Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.
assert triangle_area(-1) == None
"""

def triangle_area(radius):
    return 0 if radius <= 5 else 2 * math.pi * abs(math.sin(5)) ** (1 / 3)
