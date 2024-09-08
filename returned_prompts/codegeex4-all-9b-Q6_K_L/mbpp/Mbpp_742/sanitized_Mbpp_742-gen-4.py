def area_tetrahedron(side_length):
    """
    Calculate the area of a tetrahedron given the side length.

    :param side_length: The length of one side of the tetrahedron.
    :return: The area of the tetrahedron.
    """
    # Calculate the area of the base triangle
    base_triangle_area = (side_length ** 2 * (3 ** 0.5)) / 4

    # Calculate the height of the tetrahedron
    height = side_length * (3 ** 0.5) / 2

    # Calculate the area of the four triangular faces
    face_area = (side_length ** 2 / 4) * (1 + 2 * (3 ** 0.5))

    # Calculate the total area of the tetrahedron
    total_area = base_triangle_area + 4 * face_area

    return total_area