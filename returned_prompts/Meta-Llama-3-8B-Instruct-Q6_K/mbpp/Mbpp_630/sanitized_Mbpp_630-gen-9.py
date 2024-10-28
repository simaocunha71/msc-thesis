def get_coordinates(coordinate):
    x, y = coordinate
    return [[i, j] for i in range(x-1, x+2) for j in range(y-1, y+2) if 0 <= i <= 4 and 0 <= j <= 4] # assuming the coordinates are in a 5x5 grid
    # return [[i, j] for i in range(x-1, x+2) for j in range(y-1, y+2)] # assuming the coordinates are in a grid of any size
    # return [[x-1, y], [x-1, y-1], [x-1, y+1], [x, y-1], [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]] # assuming the coordinates are in a 2D grid
    # return [(x, j) for j in range(y-1, y+2)] + [(i, y) for i in range(x-1, x+2)] # assuming the coordinates are in a 2D grid
    # return [(i, j) for i in range(x-1, x+2) for j in range(y-1, y+2)] # assuming the coordinates are in a 2D grid
    # return [[i, j] for i in range(x-1, x+2) for j in range(y-1, y+2) if 0 <= i <= 4 and 0 <= j <= 4] # assuming the coordinates are in a 5x5 grid
    # return [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y], [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]] # assuming the coordinates are in a 2D grid
    # return [(x-1, y), (x, y-1), (x, y+1), (x+1, y), (x, y)] # assuming the coordinates are in a 2D grid
    # return [(x, y-1), (x, y), (x, y+1)] # assuming the coordinates are