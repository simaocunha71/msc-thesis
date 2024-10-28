def combinations_colors(colors: list,n: int) -> list:
  from itertools import combinations_with_replacement
  comb = list(combinations_with_replacement(colors, n))
  return comb

