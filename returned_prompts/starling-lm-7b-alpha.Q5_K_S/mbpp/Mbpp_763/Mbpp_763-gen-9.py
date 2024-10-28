
def find_min_diff(nums: list,target_sum: int) -> int:
  nums.sort()
  min_diff = float('inf')
  for i in range(len(nums)-1):
    if nums[i]+nums[i+1] == target_sum:
      min_diff = 0
      break
    min_diff = min(min_diff,nums[i+1]-nums[i])
  return min_diff


