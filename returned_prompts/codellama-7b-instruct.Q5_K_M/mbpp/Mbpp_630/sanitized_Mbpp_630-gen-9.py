def get_coordinates(coord):
    x, y = coord
    coords = []
    for i in range(1, 4):
        for j in range(1, 4):
            coords.append([x + i - 1, y + j - 1])
    return coords