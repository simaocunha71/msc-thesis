def max_sub_array_sum(nums, n):
    if n == 0:
        return 0
    max_sum = float('-inf')
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
    return max_sum