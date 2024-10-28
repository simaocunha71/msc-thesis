def surface_Area(base_edge, height):
    slant_height = (height**2 + (base_edge**2)/4)**0.5
    base_area = base_edge**2
    lateral_area = 2 * base_edge * slant_height
    return 2 * base_area + lateral_area