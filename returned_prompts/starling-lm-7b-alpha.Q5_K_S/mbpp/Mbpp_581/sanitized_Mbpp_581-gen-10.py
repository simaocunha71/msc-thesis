def surface_Area(base_edge, height):
    """
    Returns the surface area of a square pyramid with a given base edge and height.

    >>> assert surface_Area(3,4) == 33
    >>> assert surface_Area(2,1) == 10
    >>> assert surface_Area(4,3) == 28.867917729
    """
    return 2 * (base_edge ** 2 + (base_edge * height)**2) ** 0.5