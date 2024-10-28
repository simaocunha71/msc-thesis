
def extract_singly(nums: list) -> set:
  return set(num for sub in nums for num in sub)


