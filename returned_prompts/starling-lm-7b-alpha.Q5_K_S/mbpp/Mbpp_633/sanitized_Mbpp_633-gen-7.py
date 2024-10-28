def pair_xor_Sum(nums, k):
    s = 0
    for i in range(len(nums)):
        s ^= (nums[i] ^ k)
    return s