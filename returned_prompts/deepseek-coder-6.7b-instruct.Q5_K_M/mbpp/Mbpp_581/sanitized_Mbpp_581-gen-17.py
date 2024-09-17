def surface_Area(base, height):
    # Calculate the slant height
    slant_height = (base / 2) ** 2 + height ** 2
    # Calculate the lateral surface area
    lateral_surface_area = 2 * 3.141592653589793 * (base / 2) * slant_height
    # Calculate the base surface area
    base_surface_area = 3.141592653589793 * (base / 2) ** 2
    # Return the total surface area
    return lateral_surface_area + base_surface_area