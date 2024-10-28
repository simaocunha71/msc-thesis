def max_sum_increasing_subseq(nums:list, i:int, k:int, n:int) -> int:
  nums_new = nums[:i] + [nums[k]] + nums[i+1:n]
  max_sum = 0
  for i in range(len(nums_new)):
    max_sum = max(nums_new[i] + max(0, max_sum_increasing_subseq(nums_new, i+1, n)), max_sum)
  return max_sum