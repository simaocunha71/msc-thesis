def area_tetrahedron(volume):
    # Calculate the length of the edges using the formula
    a = (3 * volume) ** (1/3)
    b = (3 * volume) ** (1/3)
    c = (3 * volume) ** (1/3)
    d = (27 * volume ** 2) ** (1/3)
    
    # Calculate the area
    area = 1/3 * ((a+b+c+d) * (-a+b+c+d) * (a-b+c+d) * (a+b-c+d) * (a+b+c-d)) ** (1/2)
    
    return area