def second_smallest(nums: list) -> int:
  unique_nums = list(set(nums))
  unique_nums.sort()
  if len(unique_nums) < 2:
    return None
  else:
    return unique_nums[1]