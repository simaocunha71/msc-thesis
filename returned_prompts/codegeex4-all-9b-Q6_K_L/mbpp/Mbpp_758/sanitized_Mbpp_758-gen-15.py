def unique_sublists(nums):
  num_dict = {}
  for num in nums:
    num_dict[tuple(num)] = num_dict.get(tuple(num), 0) + 1
  return num_dict