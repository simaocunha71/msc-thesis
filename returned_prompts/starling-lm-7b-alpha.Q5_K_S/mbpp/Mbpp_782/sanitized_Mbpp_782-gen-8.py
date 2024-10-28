def odd_length_sum(nums):
    res = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if (j - i) % 2 == 1:
                res += sum(nums[i:j])
    return res
nums = [1, 2, 4]