
import itertools as it
def combinations_colors(lst: list, n: int) -> list:
  return list(it.product(lst, repeat=n))


