The lateral surface area of a cube is its surface area minus the area of the base. Since a cube has a square base and all its sides are equal, the lateral surface area of a cube is simply its total surface area minus the area of the base. The formula for the lateral surface area of a cube is 4 * s^2, where s is the side length of the cube.

Here is the Python function that calculates the lateral surface area of a cube:

```
def lateralsurface_cube(s):
    return 4 * s ** 2
```

This function takes the side length of the cube as input and returns its lateral surface area. The unit test `assert lateralsurface_cube(5)==100` confirms that the function works correctly. For a cube with a side length of 5, the lateral surface area is indeed 100. 