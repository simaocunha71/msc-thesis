```
def volume_cube(side_length):
    return side_length ** 3
```
The problem is asking to write a function that calculates the volume of a cube given its side length. The volume of a cube can be calculated by cubing the side length. 

The unit test provided, `assert volume_cube(3)==27`, suggests that the function should return the volume of a cube with a side length of 3, which is 27 (3^3). 

So, the solution is a simple function that takes the side length as input and returns the cube of that value. This can be achieved using the exponentiation operator `**` in Python. 

For example, `side_length ** 3` would calculate the cube of the side length and return the result. This function would pass the provided unit test. 