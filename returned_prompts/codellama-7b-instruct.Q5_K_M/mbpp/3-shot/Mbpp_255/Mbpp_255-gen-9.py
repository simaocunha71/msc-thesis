
import itertools
def combinations_colors(colors: list, n: int) -> list:
  return [tuple(i) for i in itertools.combinations(colors, n)]


