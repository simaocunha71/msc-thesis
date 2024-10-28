```
def division_elements(tuple1, tuple2):
    return tuple(i/j for i, j in zip(tuple1, tuple2))
```
This function uses the built-in Python functions zip and tuple to iterate over the elements of the input tuples in parallel. The zip function returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The division operation is performed on each pair of elements and the result is stored in a new tuple. The function returns this new tuple. 

The unit test `assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)` ensures that the function works correctly for the given input. 

Note: This function assumes that the input tuples are not empty and that the second tuple is not zero. If this is not the case, the function may raise a ZeroDivisionError or return incorrect results. You may want to add error handling to the function to handle these cases. 

For example:
```
def division_elements(tuple1, tuple2):
    if not tuple2:
        return tuple1
    result = tuple(i/j for i, j in zip(tuple1, tuple2))
    return result
``` 
This version of the function will return the original tuple if the second tuple is empty. You can add more error handling as needed. 