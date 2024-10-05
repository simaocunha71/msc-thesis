
Here's a solution to the problem:

```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This solution works by subtracting the integer part of the number from the original number to get the decimal part.

Here's an example of how to use the function:

```python
print(truncate_number(3.5))  # prints: 0.5
```

The function `truncate_number` takes a floating point number as input and returns the decimal part of the number.

For example, if we call `truncate_number(3.5)`, it will return `0.5` because `3.5 - 3 = 0.5`.

In the solution, we use the `int` function to convert the number to an integer and then subtract it from the original number to get the decimal part.

Note that the `int` function rounds down to the nearest whole number, so `int(3.5)` is equal to `3`.

This is why `number - int(number)` gives us the decimal part of the number, as it is the leftover part after removing the integer part.

I hope this helps! Let me know if you have any more questions.

```python
```

```python
```
```

Answer: Here's a solution to the problem:

```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This solution works by subtracting the integer part of the number from the original number to get the decimal part.

Here's an example of how to use the function:

```python
print(truncate_number(3.5))  # prints: 0.5
```

The function `truncate_number` takes a floating point number as input and returns the decimal part of the number.

For example, if we call `truncate_number(3.5)`, it will return `0.5` because `3.5 - 3 = 0.5`.

In the solution, we use the `int`