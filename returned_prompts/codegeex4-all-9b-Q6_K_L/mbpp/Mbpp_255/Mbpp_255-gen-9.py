import itertools
def combinations_colors(colors: list, n: int) -> list:
  return list(itertools.combinations_with_replacement(colors,n))

