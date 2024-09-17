def max_sum(nums):
  n = len(nums)
  lis = [0]*n
  lds = [0]*n

  lis[0] = nums[0]
  for i in range(1, n):
      lis[i] = max(nums[i], lis[i-1] + nums[i])

  lds[n-1] = nums[n-1]
  for i in range(n-2, -1, -1):
      lds[i] = max(nums[i], lds[i+1] + nums[i])

  max_sum = 0
  for i in range(n):
      max_sum = max(max_sum, lis[i] + lds[i] - nums[i])

  return max_sum