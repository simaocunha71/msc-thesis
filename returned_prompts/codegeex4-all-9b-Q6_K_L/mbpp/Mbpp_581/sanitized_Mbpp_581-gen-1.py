import math
def surface_Area(base_edge, height):
    base_area = base_edge ** 2
    slant_height = math.sqrt(height ** 2 + (base_edge / 2) ** 2)
    face_area = 0.5 * base_edge * slant_height
    total_area = base_area + 4 * face_area
    return total_area