def sort_sublists(nums: list) -> list:
  sorted_sublists = [sorted(sublist) for sublist in nums]
  return sorted_sublists

