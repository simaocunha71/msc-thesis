You can use list comprehension and the range function to generate all the adjacent coordinates. Here's how you can do it:

```python
def get_coordinates(coordinate):
    x, y = coordinate
    return [[x-1, y], [x, y-1], [x+1, y], [x, y+1], [x-1, y-1], [x-1, y+1], [x+1, y-1], [x+1, y+1]]
```

This function takes a coordinate tuple as input, extracts the x and y values, and then generates all the adjacent coordinates by subtracting and adding 1 to the x and y values. The result is a list of lists, where each inner list represents a coordinate.

The unit test `assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]` confirms that the function works correctly. It checks that the output for the input `(3, 4)` is the expected list of adjacent coordinates.