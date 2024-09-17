def pair_xor_Sum(nums: list, n: int) -> int:
  xor = 0
  for i in range(n):
    xor ^= nums[i]
  return (n * (xor)) + sum(nums)