def surface_Area(base, height):
    slant_height = (base**2 + height**2)**0.5
    base_area = base**2
    side_area = base * slant_height
    return 2 * base_area + 4 * side_area