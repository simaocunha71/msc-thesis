
import itertools
def combinations_colors(mylist, n):
  return list(itertools.product(mylist, repeat=n))


