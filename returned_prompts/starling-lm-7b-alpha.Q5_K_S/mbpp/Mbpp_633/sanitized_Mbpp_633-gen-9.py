def pair_xor_Sum(nums, k):
    if not nums:
        return 0
    if len(nums) == 1:
        return 0
    if len(nums) == 2:
        return k
    return pair_xor_Sum(nums[:-1], nums[-1] ^ k) + pair_xor_Sum(nums[1:], nums[0] ^ k)