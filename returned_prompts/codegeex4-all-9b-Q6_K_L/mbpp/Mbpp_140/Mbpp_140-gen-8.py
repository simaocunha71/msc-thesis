def extract_singly(nums: list) -> set:
  flattened_nums = set([num for sublist in nums for num in sublist])
  return flattened_nums

