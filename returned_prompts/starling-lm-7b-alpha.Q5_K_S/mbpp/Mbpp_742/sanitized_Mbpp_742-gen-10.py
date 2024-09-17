import math
def area_tetrahedron(s):
    """
    Calculates the area of a tetrahedron with side length s.

    Parameters
    ----------
    s : float
        The length of each side of the tetrahedron.

    Returns
    -------
    float
        The area of the tetrahedron.
    """
    # The area of a tetrahedron with side length s is
    # sqrt(2)/4 * s^2 * sqrt(3)
    return (math.sqrt(2)/4) * (s ** 2) * (math.sqrt(3))