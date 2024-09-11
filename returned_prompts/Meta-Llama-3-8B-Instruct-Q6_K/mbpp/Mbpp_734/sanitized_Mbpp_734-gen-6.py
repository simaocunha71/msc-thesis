def sum_Of_Subarray_Prod(nums):
  res = 0
  for i in range(len(nums)):
    for j in range(i, len(nums)):
      res += math.prod(nums[i:j+1])
  return res