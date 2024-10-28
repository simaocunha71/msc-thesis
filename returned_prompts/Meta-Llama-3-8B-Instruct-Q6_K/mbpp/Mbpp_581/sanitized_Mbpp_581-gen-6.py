def surface_Area(edge, height):
    # Base area
    base_area = edge ** 2
    # Slant height
    slant_height = (edge ** 2 + height ** 2) ** 0.5
    # Area of each side
    side_area = 0.5 * edge * slant_height
    # Total surface area
    total_area = base_area + 4 * side_area
    return int(total_area)  # Round down to the nearest integer