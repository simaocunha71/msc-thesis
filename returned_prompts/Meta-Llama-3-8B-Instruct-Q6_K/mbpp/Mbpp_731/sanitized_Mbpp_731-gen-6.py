import math
def lateralsurface_cone(r, h):
    lateral_surface_area = math.pi * r * (r + math.sqrt(r**2 + h**2))
    return lateral_surface_area