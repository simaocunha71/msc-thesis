
def tuple_str_int(tup_str: str) -> tuple:
  tup_str = tup_str.replace("(", "").replace(")", "")
  tup_str = tup_str.split(", ")
  return tuple(int(i) for i in tup_str)


