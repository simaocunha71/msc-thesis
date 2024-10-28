def tuple_str_int(tup_str: str) -> tuple:
  tup_str = tup_str.replace("(", "")
  tup_str = tup_str.replace(")", "")
  tup_int = tuple(map(int, tup_str.split(", ")))
  return tup_int