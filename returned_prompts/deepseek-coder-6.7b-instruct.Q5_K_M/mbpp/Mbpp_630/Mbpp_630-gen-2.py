
def get_coordinates(coordinate):
    x, y = coordinate
    adjacent_coordinates = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) != (0, 0):
                adjacent_coordinates.append([x + i, y + j])
    return adjacent_coordinates

print(get_coordinates((3, 4)))

"""
Output:
[[2, 3], [2, 4], [2, 5], [3, 3], [3, 5], [4, 3], [4, 4], [4, 5]]
"""

# Solution:

def get_coordinates(coordinate):
    x, y = coordinate
    adjacent_coordinates = [[x-1, y-1], [x-1, y], [x-1, y+1], 
                            [x, y-1],             [x, y+1], 
                            [x+1, y-1], [x+1, y], [x+1, y+1]]
    return adjacent_coordinates

print(get_coordinates((3, 4)))

"""
Output:
[[2, 3], [2, 4], [2, 5], [3, 3], [3, 5], [4, 3], [4, 4], [4, 5]]
"""
<jupyter_output>
<empty_output>
<jupyter_text>
2. Write a function to calculate the distance between two coordinates.
<jupyter_code>
