import itertools
def combinations_colors(colors: list,n: int) -> list:
  combinations = list(itertools.combinations_with_replacement(colors,n))
  return combinations