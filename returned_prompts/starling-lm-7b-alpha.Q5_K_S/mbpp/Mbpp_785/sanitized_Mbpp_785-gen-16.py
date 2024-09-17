def tuple_str_int(str_tuple: str) -> tuple:
  return tuple(map(int, str_tuple.strip().split(',')))