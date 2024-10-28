
def max_subarray_product(nums):
  max_product = nums[0]
  for i in range(1, len(nums)):
    if nums[i - 1] == 0:
      max_product = nums[i]
    else:
      max_product = max(max_product * nums[i], nums[i])
  return max_product


