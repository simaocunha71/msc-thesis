```
def tuple_modulo(t1, t2):
    return tuple((a % b) for a, b in zip(t1, t2))
```


The function `tuple_modulo` takes two tuples `t1` and `t2` of the same length. It uses the built-in `zip` function to iterate over the elements of both tuples in parallel. For each pair of elements `a` and `b`, it calculates the remainder of `a` divided by `b` using the modulo operator `%`. The results are collected in a new tuple, which is returned by the function.

The unit test `assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)` ensures that the function works correctly. It checks that the function returns the expected result when called with the given input. If the function works correctly, the assertion will pass; otherwise, it will raise an `AssertionError`.