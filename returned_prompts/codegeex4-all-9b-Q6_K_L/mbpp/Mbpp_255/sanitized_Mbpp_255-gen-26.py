def combinations_colors(lst, n):
  import itertools
  return list(itertools.combinations_with_replacement(lst, n))