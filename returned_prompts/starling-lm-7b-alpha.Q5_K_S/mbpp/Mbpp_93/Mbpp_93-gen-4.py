```
def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result
```

Explanation:

To calculate the value of 'a' to the power 'b', we can use the concept of exponentiation. In the provided solution, the function `power` takes two parameters: `base` and `exponent`. It initializes a variable `result` to 1, which will store the final result.

Next, a `for` loop is used to iterate `exponent` number of times. In each iteration, the `result` is multiplied by the `base` value. This effectively calculates the value of `base` raised to the power of `exponent`. After the loop completes, the final result is stored in the `result` variable and returned by the function.

The provided assertion `assert power(3,4) == 81` is used to verify the correctness of the `power` function. It checks if the function correctly calculates the value of 3 to the power of 4, which should be equal to 81.

Overall, the `power` function takes a `base` and an `exponent`, and returns the value of the `base` raised to the power of the `exponent`.

```python
def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result
```

This solution demonstrates a simple and efficient way to calculate the value of 'a' to the power 'b' in Python.

```python
def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result
```

The `power` function uses a `for` loop to iterate `exponent` times and multiply the `result` by the `base` value in each iteration. This calculates the value of `base` raised to the power of `exponent`. The final result is stored in the `result` variable and returned by the function.

The provided assertion `assert power(3,4) == 81` is used to verify the correctness of the `power` function. It checks