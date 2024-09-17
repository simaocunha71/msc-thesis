def surface_Area(base_edge, height):
    slant_height = (base_edge**2 + height**2)**0.5
    base_area = base_edge**2
    lateral_area = base_edge * slant_height * 4
    total_area = base_area + lateral_area
    return total_area