def find_Volume(a, b, c):
    # calculate the area of the base triangle
    base_area = 0.5 * a * b
    
    # calculate the height of the prism
    height = c
    
    # calculate the volume of the triangular prism
    volume = base_area * height
    
    return volume