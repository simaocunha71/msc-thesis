def pair_xor_Sum(nums, k):
    xor = 0
    for i in range(len(nums)):
        xor ^= nums[i]
    return k * (xor + (len(nums) % 2 == 0) * xor)