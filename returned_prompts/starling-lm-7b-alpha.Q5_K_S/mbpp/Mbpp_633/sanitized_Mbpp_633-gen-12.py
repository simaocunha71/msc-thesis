def pair_xor_Sum(nums: list,n: int) -> int:
  return sum(nums[i]^nums[i^1] for i in range(n))