import math
def volume_sphere(radius):
    """
    Find the volume of a sphere with the given radius.
    Args:
        radius: The radius of the sphere.
    Returns:
        The volume of the sphere.
    """
    return 4/3 * math.pi * math.pow(radius, 3)
radius = 10