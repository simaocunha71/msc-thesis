```
def max_product(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums: return 0

    def max_product_sub(nums, i):
        if i == 0:
            return nums[i]
        if i == 1:
            if nums[i-1] >= 0:
                return max(nums[i], nums[i]*nums[i-1])
            else:
                return nums[i]
        if i > 1:
            if nums[i-2] >= 0 and nums[i-1] >= 0:
                return max(nums[i], nums[i]*nums[i-1]*nums[i-2])
            elif nums[i-2] < 0 and nums[i-1] < 0:
                return max(nums[i], nums[i]*nums[i-1]*nums[i-2])
            else:
                return max(nums[i], nums[i-1]*nums[i])

    return max(max_product_sub(nums, i) for i in range(len(nums)))
```

Explanation:
To solve this problem, we can follow the steps below:

1. Define a function `max_product_sub` to calculate the maximum product of an increasing subsequence, given a certain index. If the index is 0, return the number itself. If the index is 1, if the previous number is non-negative, return the maximum of the current number and the product of the current and previous number. Otherwise, just return the current number. If the index is larger than 1, if the two previous numbers are both non-negative, return the maximum of the current number and the product of the current, previous two numbers. If the two previous numbers are both negative, return the maximum of the current number and the product of the previous two numbers. Otherwise, return the product of the previous two numbers.

2. In the `max_product` function, return the maximum product by calling `max_product_sub` with