def sum_even_and_even_index(nums):
    res = 0
    for i in range(0, len(nums), 2):
        if nums[i] % 2 == 0:
            res += nums[i]
    return res