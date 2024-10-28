import math
def area_tetrahedron(base_side_length):
    """
    Calculate the area of a tetrahedron.

    Parameters
    ----------
    base_side_length : float
        The length of a side of the base of the tetrahedron.

    Returns
    -------
    float
        The area of the tetrahedron.
    """
    # The area of a tetrahedron is (sqrt(2)/12) * base_side_length^2 * height
    # The height of the tetrahedron is also the square root of 3 times the side length of the equilateral triangle formed by the three edges connecting the apex of the tetrahedron to the three vertices of the base.
    # So, the area is (sqrt(2)/12) * base_side_length^2 * sqrt(3 * base_side_length)
    return (math.sqrt(2)/12) * base_side_length**2 * math.sqrt(3 * base_side_length)