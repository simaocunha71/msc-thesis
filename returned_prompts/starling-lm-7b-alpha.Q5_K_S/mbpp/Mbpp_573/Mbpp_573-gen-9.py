
def unique_product(nums:list)->int:
  unique_nums = list(set(nums))
  product = 1
  for i in unique_nums:
    product *= i
  return product


