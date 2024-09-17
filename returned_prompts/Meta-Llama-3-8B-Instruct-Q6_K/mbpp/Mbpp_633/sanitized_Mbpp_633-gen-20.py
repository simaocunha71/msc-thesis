def pair_xor_Sum(nums, target):
    xor_sum = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            xor_sum ^= (nums[i] ^ nums[j])
    return xor_sum ^ target