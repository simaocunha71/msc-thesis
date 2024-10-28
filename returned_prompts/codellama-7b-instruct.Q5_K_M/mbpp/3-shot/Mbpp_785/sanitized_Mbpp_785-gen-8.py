def tuple_str_int(s: str) -> tuple:
  return tuple(int(i) for i in s.strip("()").split(","))