def max_Product(nums: list) -> tuple:
  max_product = (1, 1)
  for i in range(len(nums)):
    for j in range(i, len(nums)):
      if nums[i] * nums[j] > max_product[0] * max_product[1]:
        max_product = (nums[i], nums[j])
  return max_product