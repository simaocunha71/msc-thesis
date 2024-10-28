def surface_Area(edge, height):
    base_Area = edge**2
    slant_height = (edge**2 + height**2)**0.5
    side_Area = edge * slant_height
    surface_Area = 4 * side_Area + base_Area
    return surface_Area