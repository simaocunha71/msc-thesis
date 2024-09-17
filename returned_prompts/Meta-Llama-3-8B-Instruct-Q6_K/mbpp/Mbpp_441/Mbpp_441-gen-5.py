```
def surfacearea_cube(size):
    return 6*size**2
```
The function `surfacearea_cube` takes a single argument `size` which is the size of the cube. The surface area of a cube is calculated by multiplying the area of each face by 6, since there are 6 faces in a cube. The area of each face is the square of the size of the cube. So, the surface area of a cube of size `size` is `6*size**2`. 

The unit test `assert surfacearea_cube(5)==150` confirms that the function is working correctly, since the surface area of a cube of size 5 is indeed 150. 