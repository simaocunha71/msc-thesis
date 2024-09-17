def find_min_diff(nums: list,num: int) -> int:
  nums.sort()
  min_diff = nums[0]+num
  for i in range(len(nums)-1):
    min_diff = min(min_diff,nums[i+1]-nums[i])
  return min_diff