```
def surfacearea_cube(size):
    return 6*size**2
```
The problem is asking to create a function that calculates the surface area of a cube. The surface area of a cube is calculated by multiplying the area of each face by the number of faces. Since all faces of a cube are squares, the area of each face is `side^2`. There are 6 faces in a cube, so the total surface area is `6*side^2`. 

The unit test `assert surfacearea_cube(5)==150` helps to clarify the problem by providing an example of the expected output. It shows that the function should return `150` when the size of the cube is `5`. This is because the surface area of a cube with a side length of `5` is `6*5^2=150`. 

The solution is a simple function that takes the size of the cube as input and returns the calculated surface area. The function uses the formula `6*size^2` to calculate the surface area. 

This function will work for any positive integer `size`, not just the example value of `5`. It will return the surface area of a cube with the specified side length. 