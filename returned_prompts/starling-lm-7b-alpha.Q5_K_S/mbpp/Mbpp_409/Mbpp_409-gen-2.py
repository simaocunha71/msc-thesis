
def min_product_tuple(nums: list) -> int:
  min_product = min(nums, key=lambda x: x[0]*x[1])
  return min_product[0]*min_product[1]


