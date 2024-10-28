from itertools import combinations_with_replacement as cwr
def combinations_colors(colors, n):
  combs = cwr(colors, n)
  return list(combs)