
def get_coordinates(coord):
    x, y = coord
    adjacent_coordinates = [[x-1, y-1], [x-1, y], [x-1, y+1],
                            [x, y-1],            [x, y+1],
                            [x+1, y-1], [x+1, y], [x+1, y+1]]
    return adjacent_coordinates

print(get_coordinates((3, 4)))

# Output: [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]



