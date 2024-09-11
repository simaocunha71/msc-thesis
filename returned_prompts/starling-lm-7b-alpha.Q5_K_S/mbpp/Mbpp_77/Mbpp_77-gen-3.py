Here's a Python function that can be used to check if a number is divisible by 11:

```python
def is_Diff(n):
    return abs(n % 11) < 2
```

The function `is_Diff` takes an integer `n` as input and returns True if `n` is divisible by 11, and False otherwise. The function uses the modulus operator `%` to calculate the remainder of `n` divided by 11, and then compares this remainder to 0 and 1 using the `abs` function to ensure that the result is always positive. If the remainder is less than 2, the function returns True, indicating that the number is divisible by 11; otherwise, it returns False.

To test the function, you can use the `assert` keyword to check if the function returns the expected result for a specific input. In the example provided, `assert is_Diff(12345) == False` checks if the function correctly identifies that the number 12345 is not divisible by 11. If the assertion is true, the program will continue executing; if it is false, an `AssertionError` will be raised, indicating that the function is not working as expected.

You can replace the `assert is_Diff(12345) == False` line with other test cases to verify the function's behavior for different inputs.

```python
def is_Diff(n):
    return abs(n % 11) < 2

assert is_Diff(12345) == False
```

```python
def is_Diff(n):
    return abs(n % 11) < 2

assert is_Diff(12345) == False
```

In this example, the function `is_Diff` checks if a number is divisible by 11 by calculating the remainder when the number is divided by 11 and comparing it to 0 and 1. The function returns True if the remainder is less than 2, indicating that the number is divisible by 11, and False otherwise. The `assert` keyword is used to test the function's behavior, and if the function does not return the