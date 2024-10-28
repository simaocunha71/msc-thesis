```
def surfacearea_cube(size):
    return 6*size**2
``` 
This function takes the size of the cube as an input and returns the surface area of the cube. The surface area of a cube is 6 times the square of the size of the cube. This is because there are 6 faces in a cube and each face is a square with the given size. 

For example, if the size of the cube is 5, the surface area will be 6 * 5^2 = 150. This is confirmed by the unit test `assert surfacearea_cube(5)==150`. 