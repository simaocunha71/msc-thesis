def unique_sublists(nums: list) -> dict:
  unique_dict = {}
  for i in nums:
    unique_dict[tuple(i)] = nums.count(i)
  return unique_dict