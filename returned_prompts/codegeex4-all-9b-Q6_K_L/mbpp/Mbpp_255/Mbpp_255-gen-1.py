def combinations_colors(colors: list, n: int) -> list:
  return list(itertools.combinations_with_replacement(colors, n))

# Or if you want to use the solution from the book
import itertools
def combinations_colors(colors: list, n: int) -> list:
  return list(itertools.combinations(colors, n))