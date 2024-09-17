def tuple_str_int(t_str: str) -> tuple:
  return tuple(map(int, t_str.strip("()").split(",")))