
def Find_Min(nums):
  min_len = len(nums[0])
  for num in nums:
    if len(num) < min_len:
      min_len = len(num)
  return min_len


