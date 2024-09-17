"""
The lateral surface area of a cone is given by the formula πr(l+r), where l is the slant height. The slant height of a cone is given by the formula sqrt(h^2+r^2). So, the lateral surface area of a cone can be calculated as follows:

def lateralsurface_cone(r, h):
    import math
    l = math.sqrt(h**2+r**2)
    return math.pi*r*(r+l)
"""
