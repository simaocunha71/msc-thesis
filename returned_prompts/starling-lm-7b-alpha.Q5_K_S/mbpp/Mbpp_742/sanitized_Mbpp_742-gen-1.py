from math import sqrt
def area_tetrahedron(base_edge):
    """
    This function calculates the surface area of a regular tetrahedron with a given base edge length
    """
    return base_edge ** 2 * sqrt(2) / (4 * sqrt(3))