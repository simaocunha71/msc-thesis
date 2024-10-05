The minimum sum of any non-empty sub-array of nums can be found using the Kadane's algorithm. The algorithm works by iterating through the array and maintaining a running sum of the current sub-array. If the running sum becomes negative, it is reset to zero. The minimum sum is updated whenever a new minimum running sum is found.

Here is the implementation of the minSubArraySum function:

```python
def minSubArraySum(nums):
    min_sum = float('inf')
    current_sum = 0

    for num in nums:
        current_sum += num
        min_sum = min(min_sum, current_sum)
        if current_sum < 0:
            current_sum = 0

    return min_sum

print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
print(minSubArraySum([-1, -2, -3]))  # Output: -6
```