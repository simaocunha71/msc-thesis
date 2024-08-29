"""
def get_coordinates(coordinate):
    x, y = coordinate
    adjacent = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) != (0, 0):
                adjacent.append([x + i, y + j])
    return adjacent

print(get_coordinates((3, 4)))
"""

