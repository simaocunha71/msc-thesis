def surface_Area(base, height):
    # Area of square base = base * base
    base_area = base * base

    # Area of square lateral = 2 * base * height
    lateral_area = 2 * base * height

    # Surface area = Area of square base + Area of square lateral
    surface_area = base_area + lateral_area

    return surface_area

assert surface_Area(3,4) == 33

# Explanation:
# The base of the pyramid is a square with an edge length of 3, so its area is 3 * 3 = 9.
# The lateral of the pyramid is a square with a side length of 3 and height of 4, so its area is 2 * 3 * 4 = 24.
# The total surface area of the pyramid is the sum of these two areas, 9 + 24 = 33.

"""
