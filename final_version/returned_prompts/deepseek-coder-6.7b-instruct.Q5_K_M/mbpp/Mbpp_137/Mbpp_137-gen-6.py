Here is the Python function for the problem:

```python
def zero_count(arr):
    zero_count = sum(1 for num in arr if num == 0)
    non_zero_count = sum(1 for num in arr if num != 0)
    if non_zero_count != 0:
        return zero_count / non_zero_count
    else:
        return 0
```

In this function, we first count the number of zeros and non-zeros in the array using Python's built-in sum function combined with a generator expression. Then we return the ratio of zero to non-zero count. We also add a check to return 0 if there are no non-zeros to avoid division by zero.

The function call in the problem would look like this:

```python
print(math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001))
```

This would return True if the function is implemented correctly, False otherwise.
"""


def test_zero_count():
    assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
    assert math.isclose(zero_count([0, 0, 0]), 1.0, rel_tol=0.001)
    assert math.isclose(zero_count([1, 1, 1]), 0.0, rel_tol=0.001)
    assert math.isclose(zero_count([0]), 1.0, rel_tol=0.001)
    assert math.isclose(zero_count([1]), 0.0, rel_tol=0.001)
    assert math.isclose(zero_count([-1, 1