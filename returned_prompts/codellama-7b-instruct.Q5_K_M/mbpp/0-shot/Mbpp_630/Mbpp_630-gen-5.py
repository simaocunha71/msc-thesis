def get_coordinates(coordinate):
    x = coordinate[0]
    y = coordinate[1]
    coordinates = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i != x or j != y:
                coordinates.append([i, j])
    return coordinates
