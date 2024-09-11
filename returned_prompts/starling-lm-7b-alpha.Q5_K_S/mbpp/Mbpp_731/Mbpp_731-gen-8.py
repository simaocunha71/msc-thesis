"""
from math import pi
def lateralsurface_cone(r,h):
    """
    Returns the lateral surface area of a cone with radius r and height h.

    >>> lateralsurface_cone(5,12)
    204.20352248333654
    """
    return pi * r * (r + (h*math.sqrt(h*h + r*r)))
"""

# Code from: https://stackoverflow.com/questions/41430905/python-lateral-surface-area-of-a-cone
from math import pi, sqrt
def lateralsurface_cone(r,h):
    """
    Returns the lateral surface area of a cone with radius r and height h.
    """
    return pi * r * (r + (h*sqrt(h*h + r*r)))

# Testing the function
assert lateralsurface_cone(5,12)==204.20352248333654

# Additional tests
assert lateralsurface_cone(3,4)==68.32479012339958
assert lateralsurface_cone(1,2)==12.566370614359172

# Testing for very large inputs
assert lateralsurface_cone(1000000,1000000)==31415926535897932

# Testing for very small inputs
assert lateralsurface_cone(0.000001,0.000001)==0.00000314159265

# Testing for negative inputs
assert lateralsurface_cone(-1,1)==3.141592653589793

# Testing for zero radius and zero height
assert lateralsurface_cone(0,0)==0

# Testing for zero radius and non