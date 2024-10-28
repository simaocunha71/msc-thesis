
def max_Product(nums: list) -> tuple:
  max_product = nums[0] * nums[1]
  max_num = nums[0]
  for i in range(1, len(nums)):
    if nums[i] > max_num:
      max_num = nums[i]
    if nums[i] * max_num > max_product:
      max_product = nums[i] * max_num
  return (max_num, max_product)


