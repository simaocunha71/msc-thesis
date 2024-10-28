def surface_Area(base_edge, height):
    slant_height = (base_edge**2 + height**2)**0.5
    base_area = base_edge**2
    side_area = base_edge * slant_height
    top_area = (base_edge**2) / 2
    return base_area + 4 * side_area + top_area