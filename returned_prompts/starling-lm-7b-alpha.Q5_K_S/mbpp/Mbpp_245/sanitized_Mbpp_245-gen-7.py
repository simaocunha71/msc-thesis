def max_sum(nums):
    max_sum_left = [nums[0]]
    for i in range(1, len(nums)):
        max_sum_left.append(max(max_sum_left[i-1], nums[i]))
    max_sum_right = [nums[-1]]
    for i in range(len(nums)-2, -1, -1):
        max_sum_right.append(max(max_sum_right[i+1], nums[i]))
    return max(max_sum_left) + max(max_sum_right)