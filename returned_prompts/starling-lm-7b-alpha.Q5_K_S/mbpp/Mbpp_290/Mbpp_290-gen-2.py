
def max_length(nums: list) -> tuple:
  max_length = max(nums, key=len)
  return len(max_length), max_length


