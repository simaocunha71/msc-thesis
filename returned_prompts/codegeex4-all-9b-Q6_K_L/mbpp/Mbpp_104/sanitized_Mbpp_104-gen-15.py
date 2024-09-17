def sort_sublists(lst: list) -> list:
  sorted_sublists = [sorted(sublist) for sublist in lst]
  return sorted_sublists