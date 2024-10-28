def extract_singly(nums: list) -> set:
  flat_list = [item for sublist in nums for item in sublist]
  return set(flat_list)