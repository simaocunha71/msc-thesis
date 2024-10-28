def max_sub_array_sum_repeated(nums, k, max_repeats):
    total_repeats = k * max_repeats
    nums = nums * total_repeats
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum