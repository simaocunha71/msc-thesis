You can solve this problem by defining a function that takes two tuples as input and returns a new tuple where the elements are the result of subtracting the corresponding elements of the second tuple from the first tuple. Here is a Python function that does this:

```
def substract_elements(t1, t2):
    return tuple(i - j for i, j in zip(t1, t2))
```

This function uses the built-in `zip` function to iterate over the elements of the two tuples in parallel. It then uses a generator expression to subtract the corresponding elements and returns the result as a new tuple.

The unit test `assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)` ensures that the function works correctly for the given example. If the function is implemented correctly, this test should pass.