def surface_Area(base_edge, height):
    # Calculate the slant height of the pyramid
    slant_height = (base_edge**2 + height**2)**0.5
    
    # Calculate the surface area of the square base
    base_area = base_edge**2
    
    # Calculate the surface area of the 4 triangular faces
    face_area = 0.5 * base_edge * slant_height
    
    # Calculate the total surface area
    total_surface_area = base_area + 4 * face_area
    
    return total_surface_area