Here is one way you could implement this function:

```python
def sum_in_range(l, r):
    s = 0
    for i in range(l, r + 1):
        if i % 2 != 0:
            s += i
    return s
```

This function will return the sum of all odd numbers between `l` and `r` (inclusive). It does this by iterating over each number between `l` and `r` (inclusive) and checking if the number is odd. If it is, the number is added to the running total `s`.

It's important to note that the `range()` function in Python is half-open, meaning that it does not include the `r` value in the range. This is why we need to increment `r` by 1 to ensure it is included in the range.

To test this function, you can use the `assert` statement. Here's an example:

```python
def test_sum_in_range():
    assert sum_in_range(2, 5) == 8

test_sum_in_range()
```

If the function is correctly implemented, this `assert` statement will pass and return no output. If the function is incorrectly implemented, it will raise an `AssertionError` with a helpful error message indicating that the assertion failed.

```python
def test_sum_in_range():
    assert sum_in_range(2, 5) == 8

test_sum_in_range()
```

This code should return `None` if the function is correctly implemented. If the function is incorrectly implemented, it will raise an `AssertionError` with a helpful error message indicating that the assertion failed.

```python
def test_sum_in_range():
    assert sum_in_range(2, 5) == 8

test_sum_in_range()
```

Here's an example of how you could implement this function in Python:

```python
def sum_in_range(l, r):
    s = 0
    for i in range(l, r + 1):
        if i % 2 != 