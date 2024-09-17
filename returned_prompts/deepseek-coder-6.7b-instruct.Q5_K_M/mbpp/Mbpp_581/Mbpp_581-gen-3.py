
def surface_Area(base, height):
    # The surface area of a square pyramid can be calculated as (1/3)*base_area + base_perimeter*height
    base_area = base * base
    base_perimeter = 4 * base
    return (1/3) * base_area + base_perimeter * height


