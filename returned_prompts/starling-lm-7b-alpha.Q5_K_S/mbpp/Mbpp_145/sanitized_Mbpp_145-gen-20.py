def max_Abs_Diff(nums:list) -> int:
  max_difference = 0
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      max_difference = max(max_difference,abs(nums[i]-nums[j]))
  return max_difference