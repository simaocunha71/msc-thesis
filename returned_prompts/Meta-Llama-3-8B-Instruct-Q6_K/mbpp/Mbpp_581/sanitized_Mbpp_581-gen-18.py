def surface_Area(base_edge, height):
    slant_height = (base_edge**2 + height**2)**0.5
    side = base_edge
    base_area = base_edge**2
    lateral_area = 2 * base_edge * slant_height
    surface_area = base_area + lateral_area
    return surface_area