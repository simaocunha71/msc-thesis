from functools import cmp_to_key
def sort_numeric_strings(nums):
  nums.sort(key=cmp_to_key(lambda x, y: int(y) - int(x)))
  return nums