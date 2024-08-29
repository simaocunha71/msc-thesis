
def get_coordinates(coordinate):
    x, y = coordinate
    adjacent_coordinates = [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]
    return adjacent_coordinates

print(get_coordinates((3, 4)))

# Expected output:
# [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]

"""
Here, the function get_coordinates takes a coordinate tuple as input. 
It then calculates all the adjacent coordinates using a list comprehension. 
It returns a list of all adjacent coordinates.
"""

# Alternative Solution
def get_coordinates(coordinate):
    x, y = coordinate
    adjacent_coordinates = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                adjacent_coordinates.append([x+i, y+j])
    return adjacent_coordinates

print(get_coordinates((3, 4)))

# Expected output:
# [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]

"""
Here, the function get_coordinates takes a coordinate tuple as input. 
It then calculates all the adjacent coordinates using a nested loop. 
It appends each adjacent coordinate to a list and returns the list. 
The condition if i != 0 or j != 0 is used to exclude the original coordinate.
"""
<jupyter_output>
[[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4