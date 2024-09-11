"""
from math import pi
from math import sqrt

def lateralsurface_cone(r,h):
    return pi*r*sqrt(h*h+r*r)


def test_lateralsurface_cone():
    assert lateralsurface_cone(5,12)==204.20352248333654, "Test Failed"
    print("All Tests Passed")

test_lateralsurface_cone()
"""

# Alternative solution
from math import pi, sqrt
def lateralsurface_cone(r, h):
    return pi * r * sqrt(h * h + r * r)

def test_lateralsurface_cone():
    assert lateralsurface_cone(5, 12) == 204.20352248333654, "Test Failed"
    print("All Tests Passed")

test_lateralsurface_cone()


# Another alternative solution
def lateral_surface_cone(r, h):
    return pi * r * sqrt(h * h + r * r)

def test_lateral_surface_cone():
    assert lateral_surface_cone(5, 12) == 204.20352248333654, "Test Failed"
    print("All Tests Passed")

test_lateral_surface_cone()


# Yet another alternative solution
def lateral_surface_cone(r, h):
    """
    Finds the lateral surface area of a cone
    """
    return pi * r * sqrt(h ** 2 + r ** 2)

def test_lateral_surface_cone():
    """
    Test for lateral_surface_cone function
    """
    assert lateral_surface_cone(5, 12) == 204.20352248333654, "Test Failed"
    print("All Tests Passed")

test_