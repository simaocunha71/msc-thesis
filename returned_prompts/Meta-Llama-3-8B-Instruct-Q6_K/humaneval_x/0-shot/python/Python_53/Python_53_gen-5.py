    def add(x: int, y: int):
        return x + y


The function `add` takes two integer arguments `x` and `y` and returns their sum. The function is defined with type hints indicating that `x` and `y` are integers, and the return value is also an integer. The docstring provides a brief description of the function and includes doctests to verify the function's behavior. The doctests are used to check that the function behaves as expected by comparing the result of the function call with the expected output. In this case, the doctests are:

```
>>> add(2, 3)
5
>>> add(5, 7)
12
```

These doctests can be run using the Python interpreter or a testing framework like unittest to verify that the function behaves as expected. If the function behaves correctly, the tests will pass, and if the function is incorrect, the tests will fail, indicating that the function needs to be corrected.