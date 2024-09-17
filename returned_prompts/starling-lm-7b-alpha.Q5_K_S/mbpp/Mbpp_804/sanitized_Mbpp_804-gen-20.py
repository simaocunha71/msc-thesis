def is_product_even(nums:list)->bool:
  if len(nums) == 0:
    return False
  else:
    product = 1
    for i in nums:
      product *= i
    if product % 2 == 0:
      return True
    else:
      return False