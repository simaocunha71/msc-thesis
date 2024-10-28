from math import pi,sqrt
def lateralsurface_cone(r,h):
    """
    Find the lateral surface area of a cone
    """
    return pi*r*sqrt(r*r+h*h)