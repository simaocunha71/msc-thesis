def pair_xor_Sum(nums, n):
    if n > len(nums):
        return "Invalid Input"
    total_xor = 0
    for i in range(n):
        for j in range(i+1, n):
            total_xor += nums[i] ^ nums[j]
    return total_xor