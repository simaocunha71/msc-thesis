from itertools import product
def combinations_colors(colors: list,n: int) -> list:
  return list(product(colors, repeat=n))