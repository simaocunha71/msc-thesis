def pair_xor_Sum(nums: list,n: int) -> int:
  result = 0
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      result += (nums[i] ^ nums[j])
  return result