def surface_Area(base, height):
    # Volume of pyramid = (1/3) * base_area * height
    # Surface_area = 1/2 * base_area + lateral_area
    base_area = base * base
    volume = (1.0/3) * base_area * height
    lateral_area = base * (height**2)
    total_area = 0.5 * base_area + lateral_area
    return total_area