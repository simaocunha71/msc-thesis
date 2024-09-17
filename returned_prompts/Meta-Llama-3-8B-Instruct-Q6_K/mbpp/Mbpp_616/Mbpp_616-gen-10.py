```
def tuple_modulo(t1, t2):
    return tuple((a % b for a, b in zip(t1, t2)))
```





In this solution, we use the built-in `zip` function to iterate over the two tuples in parallel. For each pair of elements, we perform the modulo operation using the expression `a % b` and create a new tuple with the results. The `tuple` function is used to convert the result into a tuple.

The unit test `assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)` ensures that the function works correctly for the given input.