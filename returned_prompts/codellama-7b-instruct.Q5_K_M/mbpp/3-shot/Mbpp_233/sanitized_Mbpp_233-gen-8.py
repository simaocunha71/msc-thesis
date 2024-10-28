import math
def lateralsuface_cylinder(radius, height):
    lateral_surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius**2
    return lateral_surface_area