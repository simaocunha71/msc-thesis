
def max_subarray_product(nums):
  max_val = nums[0]
  for i in range(1, len(nums)):
    max_val = max(max_val * nums[i], nums[i])
  return max_val


