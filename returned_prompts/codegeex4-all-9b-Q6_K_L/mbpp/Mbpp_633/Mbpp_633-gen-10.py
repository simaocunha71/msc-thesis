def pair_xor_Sum(nums: list, n: int) -> int:
    return sum(i ^ j for i in nums for j in nums if i != j)