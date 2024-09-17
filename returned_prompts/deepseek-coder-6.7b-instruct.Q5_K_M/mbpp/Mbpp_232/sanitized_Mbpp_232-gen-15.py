def larg_nnum(lst: list, n: int) -> list:
  lst.sort()
  return lst[-n:]