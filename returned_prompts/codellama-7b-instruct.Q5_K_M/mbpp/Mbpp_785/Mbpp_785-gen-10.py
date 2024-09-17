
def tuple_str_int(tuple_str):
  tuple_str = tuple_str.strip("(").strip(")")
  tuple_list = tuple_str.split(",")
  tuple_int = tuple(map(int, tuple_list))
  return tuple_int


