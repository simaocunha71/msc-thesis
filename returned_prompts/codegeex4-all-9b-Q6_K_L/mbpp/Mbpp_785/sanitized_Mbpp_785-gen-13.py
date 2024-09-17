def tuple_str_int(tup_str: str) -> tuple:
  tup_list = tup_str.strip("()").split(",")
  tup_list = [int(i) for i in tup_list]
  return tuple(tup_list)