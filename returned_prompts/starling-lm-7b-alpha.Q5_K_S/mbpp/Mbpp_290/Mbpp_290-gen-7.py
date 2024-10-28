
def max_length(nums:list) -> tuple:
  max_length_nums = max(nums, key = len)
  return len(max_length_nums), max_length_nums


