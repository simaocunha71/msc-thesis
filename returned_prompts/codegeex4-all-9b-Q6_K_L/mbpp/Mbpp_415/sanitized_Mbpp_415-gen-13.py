def max_Product(nums: list) -> tuple:
  max_product = nums[0] * nums[1]
  pair = (nums[0], nums[1])
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      product = nums[i] * nums[j]
      if product > max_product:
        max_product = product
        pair = (nums[i], nums[j])
  return pair