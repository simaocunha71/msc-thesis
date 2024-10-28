def sum_Of_Subarray_Prod(nums):
  total_sum = 0
  for i in range(len(nums)):
    for j in range(i, len(nums)):
      total_sum += math.prod(nums[i:j+1])
  return total_sum