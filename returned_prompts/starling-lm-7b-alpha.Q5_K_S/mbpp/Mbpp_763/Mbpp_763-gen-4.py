
def find_min_diff(nums:list, target:int) -> int:
  nums.sort()
  return min(abs(nums[i] - nums[i-1]) for i in range(1,len(nums)))


