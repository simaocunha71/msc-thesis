def find_first_occurrence(nums: list,target: int) -> int:
  try:
    return nums.index(target)
  except ValueError:
    return -1