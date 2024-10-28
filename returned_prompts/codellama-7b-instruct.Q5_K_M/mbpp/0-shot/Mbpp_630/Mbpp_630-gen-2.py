def get_coordinates(coord):
    return [[x, y] for x in range(coord[0]-1, coord[0]+2) for y in range(coord[1]-1, coord[1]+2)]
