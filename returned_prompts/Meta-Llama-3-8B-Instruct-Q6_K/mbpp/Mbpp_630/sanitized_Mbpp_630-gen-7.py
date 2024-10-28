def get_coordinates(coordinate):
    x, y = coordinate
    coordinates = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i >= 0 and j >= 0:
                coordinates.append([i, j])
    return coordinates