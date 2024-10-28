```
def square_perimeter(side_length):
    return 4 * side_length
```
The function `square_perimeter` takes a side length as input and returns the perimeter of the square, which is the product of 4 and the side length. The unit test `assert square_perimeter(10)==40` ensures that the function works correctly for a square with a side length of 10 units. 

This function assumes that the input is a positive integer. If the input could be a non-positive integer or a non-integer, the function should handle these cases appropriately. For example, it could return an error message or raise an exception if the input is negative, or return 0 if the input is not a positive integer. 

Here is a version of the function that handles these cases:
```
def square_perimeter(side_length):
    if not isinstance(side_length, int):
        return "Error: side length must be an integer"
    if side_length <= 0:
        return "Error: side length must be a positive integer"
    return 4 * side_length
``` 