"""
def surfacearea_cube(size):
    return 6*size**2
"""
The function surfacearea_cube() takes an integer size as an argument and returns the surface area of a cube of that size. The surface area of a cube is calculated by multiplying 6 (the number of faces) by the square of the side length. The unit test provided, assert surfacearea_cube(5)==150, ensures that the function works correctly for a cube of size 5. For example, the surface area of a cube with a side length of 5 is indeed 150 (6*5^2). 

The function works by multiplying the number of faces (6) by the square of the side length (size**2). This is because each face is a square with area equal to the square of the side length, and there are 6 faces in total. The result is the total surface area of the cube. 

For example, if the input size is 5, the function will return 6*5^2 = 150. This is the surface area of a cube with a side length of 5. The function works correctly for any input size. 