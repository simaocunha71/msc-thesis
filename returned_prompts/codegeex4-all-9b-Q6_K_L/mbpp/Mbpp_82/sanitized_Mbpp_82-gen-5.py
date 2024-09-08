import math
def volume_sphere(radius):
    """
    Calculate the volume of a sphere given its radius.

    Parameters:
    radius (float): The radius of the sphere.

    Returns:
    float: The volume of the sphere.
    """
    return (4/3) * math.pi * math.pow(radius, 3)