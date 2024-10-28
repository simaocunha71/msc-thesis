def min_product_tuple(nums: list) -> int:
  min_product = min(x*y for x, y in nums)
  return min_product