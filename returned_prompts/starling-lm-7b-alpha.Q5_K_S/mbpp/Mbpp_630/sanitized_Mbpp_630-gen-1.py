def get_coordinates(coordinate):
    x, y = coordinate
    result = [(x+i,y+j) for i in range(-1, 2) for j in range(-1, 2) if (i!=0 or j!=0)]
    return result