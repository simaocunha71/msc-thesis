
To solve this problem, we can use the modulo operator (%). The modulo of a number divided by 1 gives the remainder of the division. In this case, if we divide the number by 1, the remainder will be the decimal part of the number.

Here's a step-by-step breakdown of the solution:

1. Define the function `truncate_number` that takes a `number` as input and returns a `float`.
2. Inside the function, use the modulo operator (%) to get the remainder of the division of the `number` by 1. This will give us the decimal part of the number.
3. Return the decimal part of the number as the result.

Here's an example of how to use the function:

```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    remainder = number % 1
    return remainder

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
```

In this example, the function `truncate_number` takes the number `3.5` as input and returns `0.5`, which is the decimal part of the number.

Note: The modulo operator (%) only works with integers, so we need to convert the `number` to a float using the `float()` function before applying the modulo operator.

I hope this helps! Let me know if you have any more questions.

```python
```