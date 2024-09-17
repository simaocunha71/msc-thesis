def tuple_str_int(s: str) -> tuple:
  return tuple(map(int, s.strip("()").split(",")))