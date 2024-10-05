```python
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # Initialize the minimum sum to infinity
    min_sum = float('inf')
    current_sum = 0

    # Iterate through the array
    for num in nums:
        # Update the current sum
        current_sum += num

        # Update the minimum sum if the current sum is smaller
        min_sum = min(min_sum, current_sum)

        # If the current sum becomes negative, reset it to 0
        if current_sum < 0:
            current_sum = 0

    return min_sum
```