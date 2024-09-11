"""
The volume of a sphere is given by the formula V = 4/3 * pi * r^3, where r is the radius of the sphere. Here is a function that computes the volume of a sphere:

"""

import math

def volume_sphere(radius):
    """
    Find the volume of a sphere with the given radius.
    Args:
        radius: The radius of the sphere.
    Returns:
        The volume of the sphere.
    """
    return 4/3 * math.pi * math.pow(radius, 3)

assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)

# Testing the function
radius = 10
print("The volume of the sphere with radius", radius, "is", volume_sphere(radius))

# Further testing
print("The volume of the sphere with radius", 5, "is", volume_sphere(5))
print("The volume of the sphere with radius", 2, "is", volume_sphere(2))
print("The volume of the sphere with radius", 1, "is", volume_sphere(1))
print("The volume of the sphere with radius", 0.5, "is", volume_sphere(0.5))
print("The volume of the sphere with radius", 0.1, "is", volume_sphere(0.1))
print("The volume of the sphere with radius", 0.01, "is", volume_sphere(0.01))
print("The volume of the sphere with radius", 0.001, "is", volume_sphere(0.001))
print("The volume of the sphere with radius", 0.0001, "is", volume_sphere(0.0001))
print("The volume of the sphere with radius", 0.00001, "is", volume_sphere(0.00001))
print("The volume of the sphere with radius", 0.000001, "is", volume_sphere(0.00000