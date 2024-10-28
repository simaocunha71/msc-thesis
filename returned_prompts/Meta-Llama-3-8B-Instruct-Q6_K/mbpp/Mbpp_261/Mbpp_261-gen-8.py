```
def division_elements(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Tuples must have the same length")
    return tuple(i / j for i, j in zip(t1, t2))
```


This function takes two tuples as input, checks if they have the same length, and then performs element-wise division. It uses the built-in `zip` function to pair up corresponding elements from the two tuples, and then uses a generator expression to divide each pair of elements. The result is a tuple containing the results of the divisions. 

The unit test `assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)` ensures that the function works correctly for the given input. 

If the input tuples do not have the same length, the function raises a `ValueError` with a message indicating that the tuples must have the same length. 

This function assumes that the input tuples contain only numbers (integers or floats) and that the division operation is well-defined for all pairs of elements. If the input tuples contain non-numeric values, the function will raise a `TypeError`. If the tuples contain zero, the function will raise a `ZeroDivisionError`. 

You can add additional error handling or input validation as needed to make the function more robust. 