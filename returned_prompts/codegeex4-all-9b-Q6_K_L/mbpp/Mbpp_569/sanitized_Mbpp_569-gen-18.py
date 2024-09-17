def sort_sublists(list_of_lists: list) -> list:
  for i in range(len(list_of_lists)):
    list_of_lists[i].sort()
  return list_of_lists