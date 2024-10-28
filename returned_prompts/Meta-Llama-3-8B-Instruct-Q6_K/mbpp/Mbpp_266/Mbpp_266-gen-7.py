```
def lateralsurface_cube(side_length):
    return 4*side_length**2
```



This function calculates the lateral surface area of a cube by multiplying the perimeter of the square base (which is 4*side_length) by the side length (which is side_length**2). The result is the lateral surface area of the cube. The unit test `assert lateralsurface_cube(5)==100` checks that the function returns the correct result for a cube with side length 5. 

Note that the lateral surface area of a cube is the same as the surface area of the square base (which is 4*side_length**2) since there are no curved surfaces in a cube. The function can be simplified to just `return 4*side_length**2` as shown in the solution. 





