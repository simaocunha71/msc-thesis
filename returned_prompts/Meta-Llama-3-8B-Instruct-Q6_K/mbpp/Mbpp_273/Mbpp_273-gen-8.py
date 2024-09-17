You can solve this problem by defining a function that takes two tuples as input and subtracts the elements of the second tuple from the elements of the first tuple. The function should return a new tuple with the results.

Here is a Python solution for the problem:

```python
def substract_elements(tuple1, tuple2):
    return tuple(a - b for a, b in zip(tuple1, tuple2))
```

This function uses the built-in `zip` function to pair up the elements of the two tuples. It then uses a generator expression to subtract the elements of the second tuple from the elements of the first tuple. The results are collected into a new tuple, which is then returned by the function.

The unit test `assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)` ensures that the function works correctly. It checks that the function returns the expected result when the input tuples are `(10, 4, 5)` and `(2, 5, 18)`. If the function works correctly, this test should pass. If the function does not work correctly, this test will fail. You can use this test to verify that your function is working correctly.