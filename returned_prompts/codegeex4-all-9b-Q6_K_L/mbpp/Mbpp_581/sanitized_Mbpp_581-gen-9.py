def surface_Area(base_edge, height):
    s = base_edge
    l = height
    area_base = s * s
    slant_height = (s**2 + l**2)**0.5
    area_side = 2 * s * slant_height
    total_area = area_base + area_side
    return total_area