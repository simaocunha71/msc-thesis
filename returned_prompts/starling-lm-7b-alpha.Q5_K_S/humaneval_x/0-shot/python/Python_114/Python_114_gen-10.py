
# My solution: O(n) time, O(1) space
def minSubArraySum(nums):
    curr_sum = float('inf')
    min_sum = float('inf')
    for num in nums:
        curr_sum += num
        if curr_sum < min_sum:
            min_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return min_sum

# Time: O(n^2)
# Space: O(n)
def minSubArraySum(nums):
    min_sum = float("inf")
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            min_sum = min(min_sum, sum(nums[i:j+1]))
    return min_sum

# Time: O(n * sqrt(n))
# Space: O(1)
def minSubArraySum(nums):
    min_sum = float("inf")
    for i in range(len(nums)):
        curr = 0
        for j in range(i, len(nums)):
            curr += nums[j]
            if curr > nums[j]:
                curr -= nums[j]
                i = j - 1
            min_sum = min(min_sum, curr)
    return min_sum

# Time: O(n * log(sum(nums)))
# Space: O(1)
def minSubArraySum(nums):
    min_sum = float("inf")
    for i in range(len(nums)):
        curr = 0
        for j in range(i, len(nums)):
            curr += nums[j]
            if curr > nums[j]:
                curr -= nums[j]
                i = j - 1
            min_sum = min(min_sum, curr)
    return min_sum


```
```

My solution: O(n) time, O(1) space

```python
def minSubArraySum(nums):
    curr_sum = float('