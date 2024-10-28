
def find_min_diff(nums: list, target: int) -> int:
  sorted_nums = sorted(nums)
  min_diff = float("inf")
  for i in range(len(sorted_nums)-1):
    if sorted_nums[i]+1 == sorted_nums[i+1]:
      min_diff = min(min_diff, sorted_nums[i+1]-sorted_nums[i])
    elif sorted_nums[i]+1 < target:
      min_diff = min(min_diff, target-sorted_nums[i])
      break
    elif target == sorted_nums[-1]:
      min_diff = min(min_diff, target-sorted_nums[i])
      break
  return min_diff


