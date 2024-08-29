"""
def get_coordinates(t):
    x, y = t
    coordinates = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx != 0 or dy != 0:
                coordinates.append([x + dx, y + dy])
    return coordinates

print(get_coordinates((3, 4)))
"""

