def second_smallest(nums: list):
  unique_nums = list(set(nums))
  if len(unique_nums) < 2:
    return None
  unique_nums.sort()
  return unique_nums[1]