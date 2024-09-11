Here is one way to do it:

```python
def max_sub_array_sum_repeated(nums, k, t):
    res = -float('inf')
    for _ in range(t):
        res = max(res, max_sub_array_sum(nums))
    return res

def max_sub_array_sum(nums):
    max_sum = float('-inf')
    curr_sum = 0
    for num in nums:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum
```

The `max_sub_array_sum` function finds the maximum sum of a contiguous array in the given array. For the `max_sub_array_sum_repeated` function, we repeat the array `nums` `k` times and find the maximum sum of contiguous arrays in each `nums`.

This solution has a time complexity of O(n) for both functions and a space complexity of O(1).

Also, the `max_sub_array_sum` function can be optimized to O(n) time and O(1) space by using the Kadane's algorithm. Here is the optimized version:

```python
def max_sub_array_sum(nums):
    max_sum = float('-inf')
    curr_sum = 0
    for num in nums:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum
```

This version also has a time complexity of O(n) and a space complexity of O(1).

```python
def max_sub_array_sum_repeated(nums, k, t):
    res = -float('inf')
    for _ in range(t):
        res = max(res, max_sub_array_sum(nums))
    return res
```

This version also has a time complexity of O(n) and a space complexity of O(1).

Here are some test cases for the