def max_sum_increasing_subseq(nums, i, k, j):
  max_sum = 0
  for num in nums[:i]:
    if num < nums[i]:
      max_sum += num
  max_sum += nums[i]
  for num in nums[i+1:j]:
    if num > nums[i]:
      max_sum += num
  return max_sum