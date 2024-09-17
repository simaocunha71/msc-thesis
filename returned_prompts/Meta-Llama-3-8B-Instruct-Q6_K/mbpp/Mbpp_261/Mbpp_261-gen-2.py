```
def division_elements(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must be of the same length")
    return tuple(x / y for x, y in zip(tuple1, tuple2))
```


This function takes two tuples as input, checks if they are of the same length, and then performs element-wise division. It uses the built-in zip function to iterate over the two tuples in parallel and the built-in tuple function to convert the result back into a tuple. The division operation is performed using the '/' operator. If the tuples are not of the same length, it raises a ValueError. The function is tested using the unit test provided. 

The unit test `assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)` checks if the function correctly divides the elements of the first tuple by the corresponding elements of the second tuple. The expected result is `(2, 2, 2, 3)`, which is obtained by dividing `10/5`, `4/2`, `6/3`, and `9/3` respectively. 

This function assumes that the division operation will not result in a division by zero. If division by zero is possible, you may want to add error handling to deal with this case. 