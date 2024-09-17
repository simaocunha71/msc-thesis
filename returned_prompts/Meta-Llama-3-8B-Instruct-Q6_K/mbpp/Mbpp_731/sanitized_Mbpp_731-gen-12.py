import math
def lateralsurface_cone(r, h):
    slant_height = math.sqrt(r**2 + h**2)
    lateral_surface_area = math.pi * r * slant_height
    return lateral_surface_area