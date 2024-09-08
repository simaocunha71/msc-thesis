def area_tetrahedron(edge_length: float) -> float:
    """
    Calculate the area of a tetrahedron given its edge length.

    Args:
    - edge_length (float): The length of an edge of the tetrahedron.

    Returns:
    - float: The area of the tetrahedron.
    """
    return (edge_length ** 2 * (sqrt(3))) / 4