```
def surfacearea_cube(size):
    return 6*size**2
```
This function calculates the surface area of a cube by multiplying the area of each face (which is `size**2`) by the number of faces (which is 6). The `**` operator is used to raise the size to the power of 2. 

For example, if the size of the cube is 5, the surface area would be 6 * 5**2 = 6 * 25 = 150. This is confirmed by the unit test `assert surfacearea_cube(5)==150`. 