def consecutive_duplicates(nums: list) -> list:
  nums = list(dict.fromkeys(nums))
  return nums