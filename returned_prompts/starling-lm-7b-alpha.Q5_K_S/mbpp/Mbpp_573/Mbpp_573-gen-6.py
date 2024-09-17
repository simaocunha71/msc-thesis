
def unique_product(nums):
  unique_nums = set(nums)
  product = 1
  for i in unique_nums:
    product *= i
  return product


