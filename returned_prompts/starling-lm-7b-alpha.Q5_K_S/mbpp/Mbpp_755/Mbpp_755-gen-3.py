```
def second_smallest(nums):
    nums.sort()
    return nums[1]
```

Explanation:

To find the second smallest number in a list, we can follow these steps:

1. Sort the list in ascending order using the `sort()` method. This will rearrange the elements in the list such that the smallest number comes first and the largest number comes last.
2. Return the element at index 1, which will be the second smallest number in the sorted list.

In the provided solution, the `nums.sort()` line sorts the `nums` list in ascending order. Then, `nums[1]` returns the element at index 1, which is the second smallest number in the list.

The `assert` statement is used to verify the correctness of the solution. In this case, it checks if the `second_smallest` function correctly identifies the second smallest number in the given list `[1, 2, -8, -2, 0, -2]`, which is `-2`.

Overall, this solution provides a simple and efficient way to find the second smallest number in a list using Python.

```python
def second_smallest(nums):
    nums.sort()
    return nums[1]
```

This solution uses the built-in `sort()` method to sort the `nums` list in ascending order. Then, it returns the element at index 1, which is the second smallest number in the sorted list.

The `assert` statement is used to test the correctness of the solution. In this case, it checks if the `second_smallest` function correctly identifies the second smallest number in the given list `[1, 2, -8, -2, 0, -2]`, which is `-2`.

By using this solution, you can easily find the second smallest number in a list in Python.
```python
def second_smallest(nums):
    nums.sort()
    return nums[1]
```

This solution is efficient and straightforward. It uses the built-in `sort()` method to sort the `nums` list in ascending order. Then, it returns