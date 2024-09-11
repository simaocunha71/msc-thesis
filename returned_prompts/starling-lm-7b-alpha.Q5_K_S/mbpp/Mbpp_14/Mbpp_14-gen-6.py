Here is one possible solution:

```python
def find_Volume(base, height, depth):
    return 1/2 * base * height * depth
```

This function takes three parameters: the base area, the height, and the depth of the triangular prism. It then calculates and returns the volume of the prism using the formula `1/2 * base * height * depth`.

To test the function, you can call it with the given input `find_Volume(10,8,6)` and assert that the result is equal to `240`. This ensures that the function is correctly calculating the volume of the triangular prism.

```python
def find_Volume(base, height, depth):
    return 1/2 * base * height * depth

assert find_Volume(10,8,6) == 240
```

This assertion will pass if the function is correctly implemented, and fail otherwise, indicating a bug in the function's implementation.

```python
find_Volume(base, height, depth) == 240
```

Here, we are using the `==` operator to compare the result of the `find_Volume` function with the expected value of `240`. If the function is correctly implemented, this comparison will evaluate to `True`, and the assertion will pass. Otherwise, if the function's implementation has a bug, the comparison will evaluate to `False`, and the assertion will fail, alerting us to the error in the function's implementation.

```python
def find_Volume(base, height, depth):
    return 1/2 * base * height * depth
```

This is the implementation of the `find_Volume` function. It takes three parameters: `base`, `height`, and `depth`. The function calculates the volume of the triangular prism using the formula `1/2 * base * height * depth` and returns the result.

To use this function, you can call it with the appropriate values for the base area, height, and depth of the triangular prism. In this case, `find_Volume(10,8,6)` is called to calculate the volume of a triangular prism with a base area of 10,