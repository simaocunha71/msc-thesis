from itertools import combinations_with_replacement as cwr
def combinations_colors(lst: list,n: int) -> list:
  return list(cwr(lst,n))