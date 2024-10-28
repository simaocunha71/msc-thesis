def max_sum(nums):
    max_sum = 0
    for i in range(len(nums)):
        left = max_sum
        right = 0
        for j in range(i):
            right = max(right, left + nums[j])
            left += nums[j]
        max_sum = max(left, right) + nums[i]
    return max_sum