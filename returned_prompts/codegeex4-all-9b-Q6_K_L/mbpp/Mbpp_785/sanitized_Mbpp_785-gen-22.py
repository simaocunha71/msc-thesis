def tuple_str_int(tup_str):
  return tuple(map(int, tup_str.strip("()").split(",")))