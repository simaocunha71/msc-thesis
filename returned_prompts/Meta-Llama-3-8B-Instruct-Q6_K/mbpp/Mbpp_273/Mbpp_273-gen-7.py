You can solve this problem by creating a function that takes two tuples as input, and then subtracts the elements of the second tuple from the elements of the first tuple. The result will be a new tuple with the same length as the input tuples.

Here is a Python function that accomplishes this:

```
def substract_elements(t1, t2):
    return tuple(i - j for i, j in zip(t1, t2))
```

This function uses the built-in `zip` function to pair up the elements of the two input tuples, and then uses a generator expression to subtract the elements of the second tuple from the elements of the first tuple. The result is a new tuple with the same length as the input tuples.

The unit test `assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)` ensures that the function works correctly. It checks that the result of subtracting the elements of the second tuple from the elements of the first tuple is `(8, -1, -13)`, which is the expected output. If the function is implemented correctly, this test will pass. If the function is implemented incorrectly, this test will fail, indicating that there is a bug in the function.