def unique_product(nums: list) -> int:
  unique_nums = set(nums)
  product_nums = 1
  for i in unique_nums:
    product_nums *= i
  return product_nums