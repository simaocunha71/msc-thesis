def max_subarray_product(nums: list) -> int:
  product = 0
  max_product = 0
  for num in nums:
    product *= num
    max_product = max(max_product, product)
    if product < 0:
      product = 0
  return max_product