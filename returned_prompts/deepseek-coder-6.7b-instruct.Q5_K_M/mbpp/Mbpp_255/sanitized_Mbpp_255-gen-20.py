import itertools as it
def combinations_colors(lst, n):
  return list(it.product(lst, repeat=n))