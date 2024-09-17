```
def division_elements(tuple1, tuple2):
    return tuple(map(lambda x, y: x / y, tuple1, tuple2))
```


The provided unit test `assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)` indicates that the division operation should be performed element-wise across the given tuples. This means that each element from the first tuple should be divided by the corresponding element from the second tuple, and the results should be collected in a new tuple.

The given solution defines a function `division_elements` that takes two tuples as input. It uses the `map` function to apply a lambda function to each pair of elements from the two tuples. The lambda function performs the division operation and returns the result. The `map` function collects the results and returns a new tuple. This new tuple contains the element-wise division results of the input tuples.