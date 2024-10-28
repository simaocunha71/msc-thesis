def extract_singly(nums: list) -> set:
  flatten_list = []
  for i in nums:
    flatten_list.extend(i)
  return set(flatten_list)