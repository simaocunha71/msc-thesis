def max_length(list_of_lists: list) -> tuple:
  max_len = 0
  max_list = []
  for lst in list_of_lists:
    if len(lst) > max_len:
      max_len = len(lst)
      max_list = lst
  return max_len, max_list
