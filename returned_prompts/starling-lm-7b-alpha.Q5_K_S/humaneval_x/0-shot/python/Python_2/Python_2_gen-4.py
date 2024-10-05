
Here's a function that solves the problem:

```python
def truncate_number(number: float) -> float:
    return number % 1
```

Explanation:
The `%` operator in Python gives the remainder of the division of two numbers. In this case, it is used to obtain the decimal part of the given number. By dividing the number by 1, we get the remainder which corresponds to the decimal part.

For example, when we call `truncate_number(3.5)`, the function returns `0.5` as the remainder of the division of `3.5` by `1`.

To use this function, you can call it with a positive floating point number as the argument, and it will return the decimal part of that number.

```python
result = truncate_number(3.5)
print(result)  # Output: 0.5
```

This function can be used to extract the decimal part of any positive floating point number, as long as the number is passed as an argument to the function.

```python
number = 2.75
decimal_part = truncate_number(number)
print(decimal_part)  # Output: 0.75
```

In this way, the `truncate_number` function can be used to obtain the decimal part of a given positive floating point number.

```python
number = 4.125
decimal_part = truncate_number(number)
print(decimal_part)  # Output: 0.125
```

Overall, the function `truncate_number` provides a straightforward way to extract the decimal part of a given positive floating point number in Python.

```python
number = 5.678
decimal_part = truncate_number(number)
print(decimal_part)  # Output: 0.678
```

```python
number = 3.14159
decimal_part = truncate_number(number)
print(decimal_part)  # Output: 0.14159
```

```python
number = 7