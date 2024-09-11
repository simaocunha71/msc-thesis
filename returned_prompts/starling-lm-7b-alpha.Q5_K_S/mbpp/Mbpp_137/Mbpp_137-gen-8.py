Here's one way to do it:

```python
from math import isclose

def zero_count(nums):
    zero_count = 0
    for num in nums:
        if num == 0:
            zero_count += 1
    return zero_count / len(nums)
```

You can test it with `assert isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)` to ensure that it's giving you the expected result.

```python
def isclose(a, b, rel_tol=1e-09):
    return abs(a-b) <= rel_tol * max(abs(a), abs(b))
```

This function iterates over all the numbers in the array, and increments the count of zeroes if it encounters one. At the end, it returns the count of zeroes divided by the length of the array, which gives you the ratio of zeroes to non-zeroes.

The `isclose` function is used to compare the result of the `zero_count` function with the expected result, ensuring that the difference between them is within a small tolerance. This is important because floating point numbers can have rounding errors, and we want to make sure that the result is accurate to within a small margin of error.

Overall, this solution provides a straightforward way to calculate the ratio of zeroes to non-zeroes in an array of integers.
```

```python
def isclose(a, b, rel_tol=1e-09):
    return abs(a-b) <= rel_tol * max(abs(a), abs(b))
```

```python
def zero_count(nums):
    zero_count = 0
    for num in nums:
        if num == 0:
            zero_count += 1
    return zero_count / len(nums)
```
```python
assert isclose(zero_count([0, 1, 2