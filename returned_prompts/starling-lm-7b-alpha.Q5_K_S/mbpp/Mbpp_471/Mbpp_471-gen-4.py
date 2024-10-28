
def find_remainder(nums: list, mod: int) -> int:
  product = 1
  for num in nums:
    product = (product * num) % mod
  return product


