def extract_singly(nums: list) -> set:
  return set([num for sublist in nums for num in sublist])