def max_length(lst_of_lsts: list) -> tuple:
  max_len, max_lst = 0, []
  for lst in lst_of_lsts:
    if len(lst) > max_len:
      max_len = len(lst)
      max_lst = lst
  return max_len, max_lst