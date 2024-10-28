```python
def largest_subset(nums):
    nums.sort()
    max_size = 0
    for i in range(len(nums)):
        size = 1
        for j in range(i+1, len(nums)):
            if nums[j] % nums[i] == 0:
                size += 1
        max_size = max(max_size, size)
    return max_size
```