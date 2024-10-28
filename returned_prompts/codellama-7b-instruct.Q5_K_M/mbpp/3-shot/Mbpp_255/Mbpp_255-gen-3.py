
import itertools
def combinations_colors(colors,n):
  combos = list(itertools.combinations_with_replacement(colors, n))
  return list(map(tuple, combos))


