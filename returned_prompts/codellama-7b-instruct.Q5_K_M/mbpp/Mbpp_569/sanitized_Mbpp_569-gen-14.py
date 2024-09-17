def sort_sublists(my_list_of_lists: list) -> list:
  return sorted(my_list_of_lists, key=lambda x: sorted(x))