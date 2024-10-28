def get_coordinates(coordinate_tuple):
    x, y = coordinate_tuple
    coordinates = []
    for i in range(1, 3):
        for j in range(1, 3):
            coordinates.append([x + i - 1, y + j - 1])
    return coordinates