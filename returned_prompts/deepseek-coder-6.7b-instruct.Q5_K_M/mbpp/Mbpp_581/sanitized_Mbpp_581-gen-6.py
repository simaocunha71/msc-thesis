def surface_Area(base_edge, height):
    # formula for surface area of square pyramid is 1/2 * base_edge * base_edge + 1/2 * base_edge * sqrt((4*height*height) - (base_edge*base_edge))
    import math
    return 0.5 * base_edge * base_edge + 0.5 * base_edge * math.sqrt((4 * height * height) - (base_edge * base_edge))