def find_min_diff(nums: list,target: int) -> int:
  if len(nums) < target:
    return -1
  min_diff = float('inf')
  for i in range(len(nums)-target+1):
    min_diff = min(min_diff,nums[i+target-1]-nums[i])
  return min_diff