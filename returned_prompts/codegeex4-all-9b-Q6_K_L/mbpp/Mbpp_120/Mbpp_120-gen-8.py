def max_product_tuple(nums: list) -> int:
  max_product = 0
  for tup in nums:
    product = abs(tup[0] * tup[1])
    if product > max_product:
      max_product = product
  return max_product

