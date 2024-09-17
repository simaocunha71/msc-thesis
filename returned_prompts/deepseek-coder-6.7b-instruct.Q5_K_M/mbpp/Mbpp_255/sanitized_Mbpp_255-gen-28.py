import itertools
def combinations_colors(lst, n):
  return list(itertools.product(lst, repeat=n))