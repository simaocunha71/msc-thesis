def Find_Min(nums):
  min_length = min(len(sublist) for sublist in nums)
  for sublist in nums:
    if len(sublist) == min_length:
      return sublist