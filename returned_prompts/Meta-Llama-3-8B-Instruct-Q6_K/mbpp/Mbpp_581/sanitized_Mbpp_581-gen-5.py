def surface_Area(base, height):
    # Calculate the slant height
    slant_height = (base**2 + height**2)**0.5
    
    # Calculate the area of the base
    base_area = base**2
    
    # Calculate the area of the four triangular faces
    face_area = 0.5 * base * slant_height
    
    # Calculate the surface area
    surface_area = base_area + 4 * face_area
    
    return int(surface_area)  # Return the surface area as an integer