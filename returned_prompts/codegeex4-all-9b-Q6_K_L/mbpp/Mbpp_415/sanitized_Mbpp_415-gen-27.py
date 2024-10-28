def max_Product(nums: list) -> list:
  max_product = 0
  max_pair = ()
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] * nums[j] > max_product:
        max_product = nums[i] * nums[j]
        max_pair = (nums[i], nums[j])
  return max_pair