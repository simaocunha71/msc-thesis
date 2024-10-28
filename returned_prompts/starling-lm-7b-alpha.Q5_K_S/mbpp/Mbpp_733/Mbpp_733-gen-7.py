
def find_first_occurrence(nums:list, target:int) -> int:
  for i, num in enumerate(nums):
    if num == target:
      return i
  return -1


