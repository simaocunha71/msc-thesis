def triangle_area(radius):
    """
    Given the radius of a semicircle, find the area of the largest triangle that can be inscribed in it.

    Parameters
    ----------
    radius : float
        The radius of the semicircle.

    Returns
    -------
    float
        The area of the largest triangle that can be inscribed in the semicircle.

    Notes
    -----
    The largest triangle that can be inscribed in a semicircle is an isosceles triangle.
    """
    if radius < 0:
        return None
    return (3*radius*radius)/2