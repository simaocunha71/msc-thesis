def lateralsurface_cone(r, h):
    """
    lateralsurface_cone(r, h) returns the lateral surface area of a cone with radius r and height h.
    """
    return math.pi * r * math.sqrt(r*r + h*h)