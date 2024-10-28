def pair_xor_Sum(nums, n):
    sum_xor = 0
    for i in range(n):
        for j in range(i+1, n):
            sum_xor += nums[i] ^ nums[j]
    return sum_xor