import itertools
def combinations_colors(colors: list, n: int) -> list:
  comb = list(itertools.combinations_with_replacement(colors, n))
  return comb

