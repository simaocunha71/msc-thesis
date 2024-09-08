import math
def surface_Area(base_edge, height):
    # Calculate the height of the triangle
    height_slant = math.sqrt(base_edge**2 + height**2)
    
    # Calculate the area of the square base
    base_area = base_edge**2
    
    # Calculate the area of each triangular face
    face_area = (base_edge * height_slant) / 2
    
    # Calculate the total surface area
    total_area = base_area + 4 * face_area
    
    return total_area