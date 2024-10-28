
def sort_sublists(lst_of_lst_str: list) -> list:
  sorted_lst_of_lst_str = sorted(lst_of_lst_str, key=lambda x: sorted(x))
  return sorted_lst_of_lst_str


