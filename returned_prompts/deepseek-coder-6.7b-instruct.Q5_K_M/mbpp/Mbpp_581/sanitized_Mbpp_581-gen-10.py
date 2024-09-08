def surface_Area(base, height):
    # formula to calculate the surface area of a square pyramid is 1/2 * base_edge * slant_length + base_area
    slant_length = (height**2 + base**2)**0.5
    area = (1/2) * base * slant_length
    return round(area)