def sort_sublists(list_of_lists: list) -> list:
  sorted_lists = [sorted(sublist) for sublist in list_of_lists]
  return sorted_lists

