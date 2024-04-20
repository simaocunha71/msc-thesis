"""
Write a function to find the lateral surface area of a cylinder.
assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
"""
from math import sqrt, sin, cos
def lateral_surface_area_(height):
    """Calculate lateral surface area of the cylinder
    
    @param height: height of the cylinder
    @return: lateral surface area of the cylinder in square meters
        or a ValueError if provided invalid input.
    """
    try:
        return 2*math.pi*(height**2)/360
except ZeroDivisionError as e:
    print("Zero Division Error!")
    print(type(e))
    raise ValueError("Provided height is smaller than zero.") from e
