def pair_xor_Sum(nums: list,n: int) -> list:
    return sum(i ^ j for i in nums for j in nums)

