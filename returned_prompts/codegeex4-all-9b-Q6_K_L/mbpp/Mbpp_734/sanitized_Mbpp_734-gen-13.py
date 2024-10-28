def sum_Of_Subarray_Prod(nums: list) -> int:
  total_sum = 0
  for i in range(len(nums)):
    product = 1
    for j in range(i, len(nums)):
      product *= nums[j]
      total_sum += product
  return total_sum