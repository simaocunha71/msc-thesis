def new_tuple(string: str, lst: list) -> tuple:
  return tuple(lst + string.split(" "))