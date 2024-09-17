def surface_Area(edge, height):
    """
    Calculate the surface area of a square pyramid with a given edge length and height.

    Parameters:
    edge (int): The length of a side of the square base.
    height (int): The height of the pyramid.

    Returns:
    int: The surface area of the pyramid.
    """
    return edge * edge + 4 * edge * height