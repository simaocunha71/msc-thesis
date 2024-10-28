def pair_xor_Sum(nums, n):
    result = 0
    for i in range(n):
        for j in range(i+1, n):
            result ^= nums[i] ^ nums[j]
    return result