def max_product(nums: list) -> int:
  max_product = 1
  curr_max = nums[0]
  for i in range(1, len(nums)):
    if curr_max < nums[i]:
      curr_max = nums[i]
      max_product *= curr_max
  return max_product