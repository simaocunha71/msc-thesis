def get_coordinates(coordinate):
    # coordinates = []
    # for i in range(coordinate[0] - 1, coordinate[0] + 2):
    #     for j in range(coordinate[1] - 1, coordinate[1] + 2):
    #         coordinates.append([i, j])
    # return coordinates
    return [[x, y] for x in range(coordinate[0] - 1, coordinate[0] + 2) for y in range(coordinate[1] - 1, coordinate[1] + 2)]