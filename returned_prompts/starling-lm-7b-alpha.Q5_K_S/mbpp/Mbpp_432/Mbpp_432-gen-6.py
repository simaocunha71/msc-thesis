Here is one possible way to implement this:

```python
def median_trapezium(a, b, c):
    """
    Find the median length of a trapezium

    Parameters:
    a (int): one of the base of the trapezium
    b (int): the other base of the trapezium
    c (int): the height of the trapezium

    Returns:
    int: the median length of the trapezium
    """
    # The median length of a trapezium is half of the height times the sum of the bases, divided by 2
    return (c * (a + b)) / 2
```

This implementation follows the mathematical definition of the median length of a trapezium, which is half of the height times the sum of the bases, divided by 2. Here, `a` and `b` are the two bases of the trapezium, and `c` is the height.

To use the function, you can call it with the appropriate arguments and store the result in a variable:

```python
result = median_trapezium(15, 25, 35)
```

Finally, you can check that the result is correct by using the `assert` statement:

```python
assert result == 20
```

This will raise an `AssertionError` if the result is not equal to 20, indicating that the function is not working correctly.

```python
def median_trapezium(a, b, c):
    """
    Find the median length of a trapezium

    Parameters:
    a (int): one of the base of the trapezium
    b (int): the other base of the trapezium
    c (int): the height of the trapezium

    Returns:
    int: the median length of the trapezium
    """
    # The median length of a trapezium is half of the height times the sum of the bases, divided by 2
    return (c * (a + b)) / 2

result = median_trapezium(15, 25, 3