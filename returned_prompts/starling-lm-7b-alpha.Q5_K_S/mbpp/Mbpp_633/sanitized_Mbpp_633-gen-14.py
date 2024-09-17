def pair_xor_Sum(nums: list, n: int) -> int:
  xor_sum = 0
  for i in range(0,n):
    for j in range(i+1,n):
      xor_sum += nums[i]^nums[j]
  return xor_sum