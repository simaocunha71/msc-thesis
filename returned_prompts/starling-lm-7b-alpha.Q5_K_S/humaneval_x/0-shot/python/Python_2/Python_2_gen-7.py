
Here's a solution in Python:

```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)
```

To use this function, you can simply call it and pass the desired number as an argument. For example, to get the decimal part of 3.5, you can do:

```python
result = truncate_number(3.5)
print(result)  # Output: 0.5
```

The `int()` function is used to convert the number to an integer by rounding down to the nearest whole number. Subtracting this integer from the original number gives us the decimal part.

It's important to note that this solution assumes the input number is always positive. If you need to handle negative numbers or zero, you can add additional logic to the function.

Additionally, this solution only works for numbers with a single decimal point. If you need to handle numbers with multiple decimal points, you can modify the function to use the `round()` function instead of `int()`. This will round the number to the specified number of decimal places before subtracting it from the original number.

Overall, this solution provides a simple and straightforward way to extract the decimal part of a positive floating point number in Python.

```python
```

Here's an example of how to use the `truncate_number` function in Python:

```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)
```

To use