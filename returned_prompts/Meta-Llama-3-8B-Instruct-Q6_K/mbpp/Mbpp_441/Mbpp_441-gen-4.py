```
def surfacearea_cube(size):
    return 6 * size ** 2
```


The problem is asking you to write a function that calculates the surface area of a cube. The cube's size is given as an input to the function. 

The surface area of a cube is calculated by taking the perimeter of one side, which is 4 * side length, and multiplying it by the number of sides, which is 6. So, the formula for the surface area of a cube is 6 * side length ** 2.

The unit test `assert surfacearea_cube(5)==150` helps in understanding the problem better. It indicates that the function should return 150 when the input is 5, which is the surface area of a cube with a side length of 5 (6 * 5 ** 2 = 150). 

Here is the Python function that solves the problem:
```
def surfacearea_cube(size):
    return 6 * size ** 2
```


This function takes an integer `size` as input, calculates the surface area of a cube with that size, and returns the result. The surface area is calculated using the formula 6 * side length ** 2. The function passes the given unit test, which confirms its correctness. 