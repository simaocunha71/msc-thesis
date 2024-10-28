def pair_xor_Sum(nums: list, n: int) -> int:
    total = 0
    for i in range(n):
        for j in range(i+1, n):
            total += nums[i] ^ nums[j]
    return total

