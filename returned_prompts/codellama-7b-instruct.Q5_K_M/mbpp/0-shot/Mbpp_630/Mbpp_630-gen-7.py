def get_coordinates(coordinates):
    adjacent_coordinates = []
    for x in range(coordinates[0] - 1, coordinates[0] + 2):
        for y in range(coordinates[1] - 1, coordinates[1] + 2):
            adjacent_coordinates.append([x, y])
    return adjacent_coordinates

