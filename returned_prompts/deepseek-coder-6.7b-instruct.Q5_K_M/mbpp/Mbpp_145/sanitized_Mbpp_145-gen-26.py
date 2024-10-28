def max_Abs_Diff(nums):
  return max(abs(nums[i]-nums[j]) for i in range(len(nums)) for j in range(i+1,len(nums)))