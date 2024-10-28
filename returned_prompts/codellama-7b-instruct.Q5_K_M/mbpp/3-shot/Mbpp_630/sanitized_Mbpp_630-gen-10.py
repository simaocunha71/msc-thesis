def get_coordinates(coordinate_tuple: tuple) -> list:
    x_coordinate, y_coordinate = coordinate_tuple
    coordinates = []
    for x in range(x_coordinate - 1, x_coordinate + 2):
        for y in range(y_coordinate - 1, y_coordinate + 2):
            coordinates.append([x, y])
    return coordinates