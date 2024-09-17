import math
def lateralsurface_cone(r,h):
    """
    Finds the lateral surface area of a cone

    Parameters
    ----------
    r : int or float
        The radius of the cone
    h : int or float
        The height of the cone

    Returns
    -------
    float
        The lateral surface area of the cone
    """
    return math.pi * r * (math.sqrt(h*h+r*r))