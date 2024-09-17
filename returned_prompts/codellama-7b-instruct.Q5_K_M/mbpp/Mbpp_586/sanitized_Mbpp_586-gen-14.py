def split_Arr(my_list: list, n: int) -> list:
  first_part = my_list[:n]
  last_part = my_list[n:]
  return last_part + first_part