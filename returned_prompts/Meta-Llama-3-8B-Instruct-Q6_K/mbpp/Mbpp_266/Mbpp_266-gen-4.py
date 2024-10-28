```
def lateralsurface_cube(side_length):
    if not isinstance(side_length, int) or side_length <= 0:
        raise ValueError("side_length must be a positive integer")
    return 4 * side_length ** 2
```





The function `lateralsurface_cube` calculates the lateral surface area of a cube given its side length. It takes an integer as input and returns the lateral surface area.

The lateral surface area of a cube is the area of all its sides, which is the same as the area of one side multiplied by the number of sides. The area of one side is the product of the side length and itself, which is `side_length ** 2`. There are 4 sides in a cube, so the lateral surface area is `4 * side_length ** 2`.

The function first checks if the input `side_length` is a positive integer. If not, it raises a `ValueError`. If the input is valid, it returns the lateral surface area.

The unit test `assert lateralsurface_cube(5)==100` ensures that the function works correctly for a cube with a side length of 5. The lateral surface area of such a cube is indeed 100.