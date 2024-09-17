def unique_product(nums: list) -> int:
  unique_nums = list(set(nums))
  product = 1
  for num in unique_nums:
    product *= num
  return product