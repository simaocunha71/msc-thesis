def max_Product(nums: list) -> tuple:
  max_product = (0, 0)
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      product = nums[i] * nums[j]
      if product > max_product[0] * max_product[1]:
        max_product = (nums[i], nums[j])
  return max_product