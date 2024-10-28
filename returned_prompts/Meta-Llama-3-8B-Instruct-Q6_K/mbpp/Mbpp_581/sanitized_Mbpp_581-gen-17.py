def surface_Area(base_edge, height):
    # Calculate the slant height
    slant_height = (base_edge**2 + height**2)**0.5
    
    # Calculate the area of the base
    base_area = base_edge**2
    
    # Calculate the area of each triangular face
    face_area = 0.5 * base_edge * slant_height
    
    # Calculate the total surface area
    surface_area = base_area + 4 * face_area
    
    return surface_area