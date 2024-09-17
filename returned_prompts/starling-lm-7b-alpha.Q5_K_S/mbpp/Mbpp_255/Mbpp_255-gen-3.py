
from itertools import product
def combinations_colors(colors: list, length: int) -> list:
  return list(product(colors, repeat=length))


