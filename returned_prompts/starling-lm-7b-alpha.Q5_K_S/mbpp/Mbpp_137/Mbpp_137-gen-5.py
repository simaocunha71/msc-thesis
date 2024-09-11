Here's a possible solution. We can use the `count()` method to find the number of zeroes and non-zeroes in the array, and then return the ratio of the two.

```python
def zero_count(nums):
    zero_count = nums.count(0)
    non_zero_count = len(nums) - zero_count
    return zero_count / non_zero_count
```

This function first counts the number of zeroes in the array using the `count()` method, and then subtracts this count from the total length of the array to obtain the number of non-zeroes. Finally, it returns the ratio of zeroes to non-zeroes.

To test the function, we can use the provided `assert` statement:

```python
import math

assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
```

This `assert` statement checks if the ratio of zeroes to non-zeroes returned by the `zero_count` function is approximately equal to 0.181818, with a relative tolerance of 0.001. If the condition is true, the assertion passes; otherwise, an `AssertionError` is raised.

Overall, this solution provides a straightforward way to find the ratio of zeroes to non-zeroes in an array of integers.

```python
def zero_count(nums):
    zero_count = nums.count(0)
    non_zero_count = len(nums) - zero_count
    return zero_count / non_zero_count
```

Here's an example of how you can use this function:

```python
nums = [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]
print(zero_count(nums))  # Output: 0.18181818