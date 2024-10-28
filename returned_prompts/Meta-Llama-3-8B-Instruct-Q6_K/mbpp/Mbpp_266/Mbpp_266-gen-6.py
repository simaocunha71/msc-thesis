The lateral surface area of a cube is the surface area excluding the top and bottom faces. For a cube with side length s, the lateral surface area is 4 * s^2.

Here is the Python function that calculates the lateral surface area of a cube given its side length:

```
def lateralsurface_cube(s):
    return 4 * s**2
```


This function takes a side length s as an argument and returns the lateral surface area of the cube. The unit test `assert lateralsurface_cube(5)==100` ensures that the function works correctly for a cube with side length 5, and thus for any side length.