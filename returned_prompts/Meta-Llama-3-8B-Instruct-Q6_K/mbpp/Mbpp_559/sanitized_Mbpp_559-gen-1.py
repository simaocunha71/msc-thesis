def max_sub_array_sum(nums, n):
    if n > len(nums):
        return "Invalid input: n should be less than or equal to the length of the list"
    max_sum = current_sum = sum(nums[:n])
    for i in range(n, len(nums)):
        current_sum = current_sum - nums[i - n] + nums[i]
        max_sum = max(max_sum, current_sum)
    return max_sum