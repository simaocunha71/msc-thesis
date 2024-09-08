def find_Volume(a, b, c):
    """Calculate the volume of a triangular prism."""
    # Calculate the area of the base triangle
    base_area = 0.5 * a * b
    # Calculate the height of the prism
    height = c
    # Calculate the volume of the prism
    volume = base_area * height
    return volume