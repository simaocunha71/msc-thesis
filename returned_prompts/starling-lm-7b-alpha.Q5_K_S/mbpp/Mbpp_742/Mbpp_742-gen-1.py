from math import sqrt

def area_tetrahedron(base_edge):
    """
    This function calculates the surface area of a regular tetrahedron with a given base edge length
    """
    return base_edge ** 2 * sqrt(2) / (4 * sqrt(3))

# Testing the function
print(area_tetrahedron(3))




















"""
In a regular tetrahedron, all four edges are of equal length.

The four vertices of a regular tetrahedron are connected by three pairs of edges to form four equilateral triangles.
The area of an equilateral triangle can be calculated using the formula:

    Area = (s^2 * sqrt(3)) / 4

where s is the length of a side of the equilateral triangle.

The surface area of a regular tetrahedron can be calculated by summing the areas of the four equilateral triangles.

The side length of all four triangles is equal to the base edge length of the tetrahedron.

The surface area of a regular tetrahedron with base edge length s is therefore:

    Area = 4 * [(s^2 * sqrt(3)) / 4]

    Area = s^2 * sqrt(3)

"""


"""
The surface area of a regular tetrahedron is equal to the square of its base edge length times the square root of three.

To write a function that calculates the surface area of a regular tetrahedron, you can simply multiply the square of the base edge length by the square root of three, and return the result.
"""

def area_tetrahedron(base_edge):
    """
    This function calculates the surface area of a regular tetrahedron with a given base edge length
    """
    return base_edge ** 2 * sqrt(3)

# Testing the function
print(area_tetrahedron(3))

"""
The surface area of a regular tetrahedron is equal to the square of its base edge