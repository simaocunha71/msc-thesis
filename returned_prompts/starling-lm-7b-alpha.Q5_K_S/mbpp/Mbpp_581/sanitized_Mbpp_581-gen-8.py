import math
def surface_Area(edge, height):
    """
    This function returns the surface area of a square pyramid with a given base edge and height.
    """
    return (edge * height) + (edge * edge) * (math.sqrt(2))