from itertools import product
def combinations_colors(nums, n):
  return list(product(nums, repeat=n))