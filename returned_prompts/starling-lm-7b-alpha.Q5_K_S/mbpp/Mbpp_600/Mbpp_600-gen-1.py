Here's a Python function that checks whether a given number is even or not:

```python
def is_Even(n):
    """
    Determines if a given number is even or not.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is even, False if it is not.
    """
    return n % 2 == 0
```

To use this function, you can call it with a number as an argument, like this:

```python
print(is_Even(1))  # Prints: False
```

In the function, `n % 2` calculates the remainder of `n` divided by 2. If the result is 0, the number is even; otherwise, it's odd. The function returns `True` if the number is even, and `False` if it's not.

To test the function, you can use the `assert` statement to check the expected output for a specific input. In this case, `assert is_Even(1) == False` asserts that the function should return `False` when given the number 1. If the assertion fails, an `AssertionError` will be raised.

Here's an example of how you can use the `assert` statement to test the function:

```python
assert is_Even(1) == False
```

If the `is_Even` function correctly identifies the number as even or not, the `assert` statement will not raise an error and the program will continue running. Otherwise, an `AssertionError` will be raised, indicating that the function's output does not match the expected result.

This kind of testing helps ensure that the function is working correctly and produces the expected results.

```python
def is_Even(n):
    """
    Determines if a given number is even or not.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is even, False if it is not.
    """
    return n % 2 == 0
```

This function works by checking the remainder of a number divided by 2 using