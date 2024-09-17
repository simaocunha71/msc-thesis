def pair_xor_Sum(nums:list,n: int) -> int:
  xor_sum = 0
  for i in range(len(nums)):
    xor_sum += n^nums[i]
  return xor_sum