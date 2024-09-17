
def pair_xor_Sum(nums, expected_sum):
    result = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            result ^= nums[i] ^ nums[j]
    return result == expected_sum


