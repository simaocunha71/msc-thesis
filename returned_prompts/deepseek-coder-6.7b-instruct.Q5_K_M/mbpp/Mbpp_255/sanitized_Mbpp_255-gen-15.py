import itertools
def combinations_colors(lst: list,n: int) -> list:
  return list(itertools.product(lst, repeat=n))