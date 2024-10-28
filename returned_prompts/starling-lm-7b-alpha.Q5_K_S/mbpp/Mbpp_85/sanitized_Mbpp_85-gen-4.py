import math
def surfacearea_sphere(r):
    """
    Find the surface area of a sphere.
    Args:
        r (float): Radius of the sphere.
    Returns:
        float: Surface area of the sphere.
    """
    # Calculate the surface area of the sphere
    surface_area = 4 * math.pi * r ** 2
    return surface_area