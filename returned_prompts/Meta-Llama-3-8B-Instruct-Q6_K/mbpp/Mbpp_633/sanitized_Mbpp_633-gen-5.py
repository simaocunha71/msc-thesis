def pair_xor_Sum(nums, k):
    pair_sum = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            pair_sum += nums[i] ^ nums[j]
    return pair_sum