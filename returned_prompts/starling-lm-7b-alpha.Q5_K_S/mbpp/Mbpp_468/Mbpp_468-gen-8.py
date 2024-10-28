
def max_product(nums: list) -> int:
  max_product = 0
  for i in range(len(nums)):
    if i == 0:
      max_product = nums[i]
    else:
      if nums[i-1] < nums[i]:
        max_product = max(max_product*nums[i], nums[i])
  return max_product


