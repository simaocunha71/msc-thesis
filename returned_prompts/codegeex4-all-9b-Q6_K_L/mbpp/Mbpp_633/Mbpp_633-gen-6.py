def pair_xor_Sum(nums: list, n: int) -> int:
    nums.sort()
    sum = 0
    for i in range(n):
        sum += nums[i] ^ nums[n-1-i]
    return sum

