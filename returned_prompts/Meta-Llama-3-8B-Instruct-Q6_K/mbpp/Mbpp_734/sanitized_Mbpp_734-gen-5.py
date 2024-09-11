def sum_Of_Subarray_Prod(nums):
  n = len(nums)
  total_sum = 0
  for i in range(n):
    for j in range(i, n):
      total_sum += math.prod(nums[i:j+1])
  return total_sum