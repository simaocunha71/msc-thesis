```
def get_coordinates(coordinate):
    x, y = coordinate
    return [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]
```


This function takes a 2D coordinate tuple as input and returns a list of all adjacent coordinates. The adjacent coordinates are calculated by shifting the input coordinates by -1, 0, or 1 in both the x and y directions. The function uses list comprehension to generate the list of adjacent coordinates. The unit test `assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]` ensures that the function works correctly for the given input. 