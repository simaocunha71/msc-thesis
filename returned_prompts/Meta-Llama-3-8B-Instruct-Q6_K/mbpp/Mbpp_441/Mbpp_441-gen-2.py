```
def surfacearea_cube(size):
    return 6*size**2
```


The function surfacearea_cube takes one argument, size, which is the length of the cube. The surface area of a cube is calculated by multiplying the number of faces (6) by the area of each face (which is size^2). 

The unit test `assert surfacearea_cube(5)==150` helps to ensure the function is working correctly. It checks that the surface area of a cube with a size of 5 is 150, which is the expected result. 

For example, if you call `surfacearea_cube(5)`, it will return `6*5**2`, which is 150. 





