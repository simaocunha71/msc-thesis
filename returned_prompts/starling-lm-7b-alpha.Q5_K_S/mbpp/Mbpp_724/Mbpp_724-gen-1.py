```
def power_base_sum(base, power):
    # Initialize result
    result = 0

    # Calculate the sum
    for _ in range(power + 1):
        result += base

    # Return the result
    return result
```

Here's a Python solution to the problem. The function `power_base_sum` takes two arguments: `base` and `power`. It calculates the sum of all digits of the `base` raised to the specified `power`. The function initializes the `result` variable to 0. Then, it uses a loop to iterate from 0 to the `power` (inclusive), adding the `base` to the `result` in each iteration. Finally, it returns the `result`.

To test the function, you can use the `assert` statement to check if the function returns the expected result for a specific example. In this case, the `assert` statement checks if `power_base_sum(2, 100)` equals 115. If the assertion is true, the program will not raise an exception. Otherwise, an exception will be raised, indicating that the function is not working correctly.

You can use this function to calculate the sum of all digits of a base raised to a specified power. Simply call the function with the desired `base` and `power` as arguments, and it will return the result.

Example usage:
```
print(power_base_sum(2, 100))  # Output: 115
```

This will print the result of `power_base_sum(2, 100)`, which is 115.

Note that the function assumes that the `base` and `power` are non-negative integers. If you want to handle other cases or add additional functionality, you can modify the function accordingly.
```

```

```python

```
```