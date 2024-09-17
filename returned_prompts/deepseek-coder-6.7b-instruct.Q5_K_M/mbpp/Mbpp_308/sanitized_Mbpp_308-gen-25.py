import itertools
def large_product(a, b, n):
  products = sorted(itertools.starmap(lambda x,y: x*y, itertools.product(a, b)), reverse=True)
  return products[:n]