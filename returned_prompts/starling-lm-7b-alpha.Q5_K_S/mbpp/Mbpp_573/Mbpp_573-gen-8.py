
def unique_product(nums: list) -> int:
  product = 1
  unique_nums = set(nums)
  for i in unique_nums:
    product *= i
  return product


