def surface_Area(base_edge, height):
    base_area = base_edge ** 2
    slant_height = (base_edge ** 2 + height ** 2) ** 0.5
    side_area = 4 * (base_edge * slant_height) / 2
    total_surface_area = base_area + side_area
    return total_surface_area