def _sum(nums):
    total = 0
    for n in nums:
        total += n
    return total

# assert _sum([1, 2, 3]) == 6

def test_sum():
    assert _sum([1, 2, 3]) == 6
    assert _sum([-1, 0, 1, 2, 3]) == 6
    assert _sum([]) == 0
    assert _sum([5]) == 5
    assert _sum([5, 5, 5, 5]) == 20

test_sum()

# _sum([1, 2, 3]) == 6
# _sum([-1, 0, 1, 2, 3]) == 6
# _sum([]) == 0
# _sum([5]) == 5
# _sum([5, 5, 5, 5]) == 20

"""
"""

```
def _sum(nums):
    total = 0
    for n in nums:
        total += n
    return total

# assert _sum([1, 2, 3]) == 6

def test_sum():
    assert _sum([1, 2, 3]) == 6
    assert _sum([-1, 0, 1, 2, 3]) == 6
    assert _sum([]) == 0
    assert _sum([5]) == 5
    assert _sum([5, 5, 5, 5]) == 20

test_sum()
```

In the provided code, a Python function called `_sum` is defined to find the sum of an array (or list) of numbers. The function initializes a variable `total` to 0, and then iterates through each element `n` in the `nums` array. For each element, it adds the value of `n` to the `total` variable. Finally, the function returns the total sum.

The `test_sum` function is also defined to test the `_sum` function with different input cases. It uses the built-in `assert` statement to check if the output of `