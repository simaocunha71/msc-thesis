```
def lateralsurface_cube(side_length):
    return 4*(side_length**2)
```


The lateral surface area of a cube is equal to the area of four faces, each of which is a square with side length equal to the cube's side length. The area of each square is side_length^2, so the lateral surface area is 4 * side_length^2. The unit test provided, assert lateralsurface_cube(5)==100, confirms this calculation. The function `lateralsurface_cube` takes the side length of the cube as input and returns its lateral surface area. The calculation is performed using the formula 4 * side_length^2. This function can be used to find the lateral surface area of a cube given its side length. For example, if the side length of the cube is 5, the function would return 100, which is the lateral surface area of a cube with a side length of 5.