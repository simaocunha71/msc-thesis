def pair_xor_Sum(nums, k):
    res = 0
    for i in range(len(nums)):
        res ^= nums[i]
    for i in range(k):
        res ^= nums[i]
        for j in range(i + 1, k):
            res ^= nums[j]
            res ^= nums[j] ^ nums[i]
    return res