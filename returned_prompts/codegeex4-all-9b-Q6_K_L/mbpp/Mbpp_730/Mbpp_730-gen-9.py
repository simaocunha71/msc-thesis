def consecutive_duplicates(nums: list) -> list:
  return list(filter(lambda x: nums.count(x)==1, nums))

