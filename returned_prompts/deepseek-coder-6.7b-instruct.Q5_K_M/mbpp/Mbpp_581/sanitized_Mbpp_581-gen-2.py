def surface_Area(base_edge, height):
    # calculate the slant height
    slant_height = (height**2 + (base_edge/2)**2)**0.5

    # calculate the area of the base
    base_area = base_edge * base_edge

    # calculate the area of the sides
    side_area = 0.5 * 4 * base_edge * slant_height

    # the surface area is the sum of the base area and the side areas
    surface_area = base_area + side_area

    return surface_area