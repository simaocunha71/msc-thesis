def pair_xor_Sum(nums, k):
    nums.sort()
    total_xor_sum = 0
    for i in range(len(nums) - 1):
        total_xor_sum += nums[i] ^ nums[i + 1]
    return total_xor_sum