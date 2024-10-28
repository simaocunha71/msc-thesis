def sum_range_list(nums, low_index, high_index):
    total = 0
    for i in range(low_index, high_index + 1):
        total += nums[i]
    return total