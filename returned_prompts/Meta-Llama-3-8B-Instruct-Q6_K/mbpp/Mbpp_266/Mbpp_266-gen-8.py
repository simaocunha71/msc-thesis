```
def lateralsurface_cube(side_length):
    lateral_surface_area = 4 * side_length ** 2
    return lateral_surface_area
```



The problem is asking to write a function that calculates the lateral surface area of a cube given its side length. The lateral surface area of a cube is the area of its four rectangular sides. 

The unit test `assert lateralsurface_cube(5)==100` suggests that the lateral surface area of a cube with side length 5 is 100. This means that each side of the cube has an area of 100/4 = 25, which is the area of a rectangle with length and width both equal to the side length of the cube.

The formula to calculate the lateral surface area of a cube is 4 times the area of one of its sides. The area of a rectangle with length and width both equal to the side length of the cube is side_length ** 2. Therefore, the lateral surface area of the cube is 4 * side_length ** 2.

Here is the Python function that implements this formula:
```
def lateralsurface_cube(side_length):
    lateral_surface_area = 4 * side_length ** 2
    return lateral_surface_area
```



This function takes the side length of the cube as input and returns its lateral surface area. The unit test `assert lateralsurface_cube(5)==100` passes with this function.