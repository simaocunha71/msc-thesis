def is_product_even(nums: list) -> bool:
  product = 1
  for num in nums:
    product *= num
  if product % 2 == 0:
    return True
  else:
    return False