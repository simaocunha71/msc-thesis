def surface_Area(base_edge, height):
    base_Area = base_edge ** 2
    side_Area = 0.5 * 4 * base_edge * height
    return round(base_Area + side_Area, 2)