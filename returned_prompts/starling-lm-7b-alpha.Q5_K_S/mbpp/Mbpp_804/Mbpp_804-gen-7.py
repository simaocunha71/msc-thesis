
def is_product_even(nums:list) -> bool:
  if len(nums) == 0:
    return False
  return any(map(lambda x: x % 2 == 0, nums))


