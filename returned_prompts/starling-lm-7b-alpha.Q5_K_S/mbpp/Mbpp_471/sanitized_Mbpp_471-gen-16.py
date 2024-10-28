def find_remainder(nums,mod):
  result = 1
  for num in nums:
    result = (result * num) % mod
  return result