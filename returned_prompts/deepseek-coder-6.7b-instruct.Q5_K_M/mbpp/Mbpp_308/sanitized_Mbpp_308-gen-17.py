import itertools
def large_product(a, b, n):
  pairs = list(itertools.product(a, b))
  products = sorted( [ x*y for x, y in pairs ], reverse=True )
  return products[:n]