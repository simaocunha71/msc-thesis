def surface_Area(base_edge, height):
    # Calculate the slant height of the pyramid
    slant_height = (height**2 + (base_edge/2)**2)**0.5
    
    # Calculate the surface area of the pyramid
    surface_area = base_edge**2 + 4*(base_edge*slant_height/2)
    
    return surface_area