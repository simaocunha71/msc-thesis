def find_remainder(nums, mod):
  prod = 1
  for i in nums:
    prod = (prod*i) % mod
  return prod