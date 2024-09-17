def is_product_even(nums:list):
  product = 1
  for i in nums:
    product *= i
  if product % 2 == 0:
    return True
  return False