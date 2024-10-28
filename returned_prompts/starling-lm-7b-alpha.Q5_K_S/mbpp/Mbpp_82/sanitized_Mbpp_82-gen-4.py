import math
def volume_sphere(radius):
    """
    Function to find the volume of a sphere.

    Parameters
    ----------
    radius : float
        The radius of the sphere.

    Returns
    -------
    float
        The volume of the sphere.
    """
    # Calculate the volume using the formula 4/3 * pi * radius^3
    return 4 / 3 * math.pi * math.pow(radius, 3)