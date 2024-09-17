def surface_Area(base_edge, height):
    side = base_edge
    slant_height = (side**2 + height**2)**0.5
    base_area = side**2
    lateral_area = 2 * base_area + 4 * side * slant_height
    return base_area + lateral_area