def get_coordinates(coordinate):
    x, y = coordinate
    adjacent_coordinates = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i, j) != (x, y):
                adjacent_coordinates.append([i, j])
    return adjacent_coordinates