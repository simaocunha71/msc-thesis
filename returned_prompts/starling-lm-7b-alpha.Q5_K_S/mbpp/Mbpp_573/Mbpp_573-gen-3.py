
def unique_product(nums: list) -> int:
  nums = set(nums)
  product = 1
  for i in nums:
    product *= i
  return product


