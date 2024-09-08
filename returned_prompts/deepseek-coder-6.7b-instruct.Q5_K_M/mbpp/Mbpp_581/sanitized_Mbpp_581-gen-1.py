def surface_Area(base, height):
    base_Area = base * base
    slant_length = (height**2 + (base/2)**2)**0.5
    lateral_Area = base_Area * slant_length
    total_Area = base_Area + 0.5 * lateral_Area
    return total_Area