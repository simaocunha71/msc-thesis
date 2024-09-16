```python
def sum_Of_Subarray_Prod(nums):
    result = 0
    for i in range(len(nums)):
        temp = 1
        for j in range(i, len(nums)):
            temp *= nums[j]
            result += temp
    return result
```
