def sort_numeric_strings(nums: list) -> list:
  return sorted(nums, key=lambda x: int(x))