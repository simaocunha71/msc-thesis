Here is a Python solution using Kadane's algorithm:

```python
def minSubArraySum(nums):
    if not nums:
        return 0

    # Initialize current_sum and min_sum to the first element
    current_sum = min_sum = nums[0]

    for num in nums[1:]:
        # If current_sum + num is less than num, set current_sum to num
        current_sum = min(current_sum + num, num)
        # Update min_sum if current_sum is less than min_sum
        min_sum = min(min_sum, current_sum)

    return min_sum
```

This solution works by iterating through the array and keeping track of the current sum of the subarray and the minimum sum encountered so far. At each step, it updates the current sum and the minimum sum if necessary. The time complexity of this solution is O(n), where n is the length of the input array.