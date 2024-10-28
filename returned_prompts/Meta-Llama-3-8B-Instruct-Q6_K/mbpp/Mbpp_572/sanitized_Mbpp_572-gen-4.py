def two_unique_nums(nums):
  return list(set(nums))[:2] if len(nums) > 2 else set(nums)