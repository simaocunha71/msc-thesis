import math
def surface_Area(base_edge, height):
    base_area = base_edge ** 2
    slant_height = math.sqrt((base_edge/2)**2 + height**2)
    surface_area = 0.5 * base_area + 4 * 0.5 * slant_height * base_edge
    return surface_area