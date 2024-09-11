Here is one way you can define and use the function:

```python
def max_Abs_Diff(nums):
    if len(nums) < 2:
        return 0
    max_abs_diff = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            max_abs_diff = max(max_abs_diff, abs(nums[i] - nums[j]))
    return max_abs_diff
```

This function first checks if the length of the input array is less than 2. If it is, then the maximum absolute difference is 0 (because there are no elements to compare).

The function then initializes a variable `max_abs_diff` to 0. This variable will store the maximum absolute difference found so far.

The function uses two nested loops to compare each pair of elements in the array. The outer loop iterates over the range from 0 to `len(nums)-1`, and the inner loop iterates over the range from `i+1` to `len(nums)`. This ensures that each pair of elements is compared exactly once.

Inside the inner loop, the function calculates the absolute difference between the current pair of elements (`abs(nums[i] - nums[j])`) and updates `max_abs_diff` if the absolute difference is greater than the current maximum.

After both loops have finished, the function returns the maximum absolute difference found.

To test the function, you can use the `assert` statement to check if the function returns the expected result for a given input array. For example, `assert max_Abs_Diff((2,1,5,3)) == 4` will pass if the function correctly returns 4 for the input array `(2,1,5,3)`.

Note that you can add more test cases to the `assert` statement to ensure that the function works correctly for different input arrays.

```python
def max_Abs_Diff(nums):
    if len(nums) < 2:
        return 0
    max_abs_diff = 0
    for i in range(len(nums)-1):
        for j in range