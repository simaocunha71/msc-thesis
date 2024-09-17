import itertools
def combinations_colors(lst: list,n: int) -> list:
  combinations = list(itertools.product(lst, repeat=n))
  return combinations

