def max_sub_array_sum(nums, s):
    max_sum = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if sum(nums[i:j + 1]) >= s and sum(nums[i:j + 1]) > max_sum:
                max_sum = sum(nums[i:j + 1])
    return max_sum