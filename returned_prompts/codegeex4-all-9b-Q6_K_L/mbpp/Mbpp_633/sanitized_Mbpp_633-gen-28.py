def pair_xor_Sum(nums: list,n: int) -> list:
  sum = 0
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      sum += nums[i] ^ nums[j]
  return sum