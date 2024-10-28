def get_coordinates(coordinate):
    x, y = coordinate
    adjacent_coordinates = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) != (0, 0):
                adjacent_coordinates.append([x + i, y + j])
    return adjacent_coordinates