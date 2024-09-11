def surface_Area(base_edge, height):
    slant_height = (base_edge**2 + height**2)**0.5
    area = 4 * (base_edge**2) + base_edge * slant_height
    return int(area)  # convert the result to an integer