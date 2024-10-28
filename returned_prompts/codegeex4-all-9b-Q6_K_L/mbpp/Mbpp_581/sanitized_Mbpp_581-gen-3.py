def surface_Area(base_edge, height):
    base_area = base_edge ** 2
    slant_height = (height ** 2 + (base_edge / 2) ** 2) ** 0.5
    side_area = base_edge * slant_height
    total_surface_area = base_area + 2 * side_area
    return total_surface_area