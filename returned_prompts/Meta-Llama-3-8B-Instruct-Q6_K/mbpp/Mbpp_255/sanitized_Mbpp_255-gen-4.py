from itertools import product
def combinations_colors(color_list, n):
  return list(product(color_list, repeat=n))  # or use map(list, product(color_list, repeat=n)) if you need a list of lists