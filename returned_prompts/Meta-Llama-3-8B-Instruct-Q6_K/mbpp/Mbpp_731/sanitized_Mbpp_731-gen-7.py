import math
def lateralsurface_cone(r, h):
    circumference = 2 * math.pi * r
    slant_height = math.sqrt(h**2 + r**2)
    lateral_surface_area = circumference * slant_height
    return lateral_surface_area