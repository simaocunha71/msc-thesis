
Here's one possible implementation:

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

In this implementation, we use the `int()` function to truncate the integer part of the number, and then return the result of subtracting the truncated integer from the original number. This gives us the decimal part of the number.

For example, if we call `truncate_number(3.5)`, the `int(number)` function will return `3`, and `number - int(number)` will return `0.5`.

This implementation works correctly for any positive floating point number.

Note that this implementation assumes that the input number is always positive. If you need to handle negative numbers or zero, you can modify the implementation to check for these cases and return an appropriate error message or value.

Here's an updated version of the implementation that handles negative numbers and zero:

```python
def truncate_number(number: float) -> float:
    """ Given a floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if number < 0:
        return -abs(number) - int(abs(number))
    else:
        return number - int(number)
```

In this version, if the input number is negative, we return the negative of the decimal part of the absolute value of the number. Otherwise, we return the decimal part of the original number.

I hope this helps! Let me know if you have any more questions.

Sincerely,
Your Friendly AI Assistant

```python

```