def find_min_diff(nums: list,target: int) -> int:
  sorted_nums = sorted(nums)
  diff = []
  for i in range(len(nums)-1):
    diff.append(sorted_nums[i+1] - sorted_nums[i])
  return min(diff) if target in nums else -1