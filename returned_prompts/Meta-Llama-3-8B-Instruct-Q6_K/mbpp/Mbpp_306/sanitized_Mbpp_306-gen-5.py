def max_sum_increasing_subseq(nums, i, k, j):
  max_sum = 0
  for num in nums[:i]:
    if num < nums[j]:
      max_sum += num
  return max_sum + nums[j] if max_sum < nums[j] else max_sum