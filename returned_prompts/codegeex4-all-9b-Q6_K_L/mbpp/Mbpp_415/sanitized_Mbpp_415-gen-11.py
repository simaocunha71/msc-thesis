def max_Product(nums: list) -> tuple:
  max_product = float('-inf')
  pair = None
  for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
      product = nums[i] * nums[j]
      if product > max_product:
        max_product = product
        pair = (nums[i], nums[j])
  return pair