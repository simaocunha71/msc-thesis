```
def substract_elements(tuple1, tuple2):
    res = []
    for i in range(len(tuple1)):
        res.append(tuple1[i] - tuple2[i])
    return tuple(res)
```

The function `substract_elements` takes in two tuples, `tuple1` and `tuple2`. It initializes an empty list `res` to store the result. Then, it uses a `for` loop to iterate over the indices of the tuples. Inside the loop, it subtracts the elements of `tuple1` at index `i` by the elements of `tuple2` at index `i`. The result is appended to the `res` list. Finally, the function returns the result as a tuple.

To test the function, you can use the provided `assert` statement. It checks if the result of the function `substract_elements` with the input `(10, 4, 5)` and `(2, 5, 18)` is equal to `(8, -1, -13)`. If the assertion is true, it means the function is working correctly.

You can run this code in a Python environment to verify the correctness of the function.

Here's an example of how you can use this function:

```python
result = substract_elements((10, 4, 5), (2, 5, 18))
print(result)  # Output: (8, -1, -13)
```

This will produce the expected result of `(8, -1, -13)` when subtracting the elements of the first tuple by the elements of the second tuple with the same index.

```python
# Output: (8, -1, -13)
```

In this case, the first tuple `(10, 4, 5)` is subtracted from the second tuple `(2, 5, 18)`. The result is `(8, -1, -13)`, which matches the expected output.

This solution demonstrates how to subtract elements of tuples with the same index using a Python function.

```python
# Output: (