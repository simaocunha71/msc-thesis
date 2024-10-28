def tuple_str_int(tuple_str: str) -> tuple:
  return tuple(map(int, tuple_str[1:-1].split(",")))