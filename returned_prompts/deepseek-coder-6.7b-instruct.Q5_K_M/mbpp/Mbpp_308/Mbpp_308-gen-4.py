
import itertools as it
def large_product(lst1, lst2, n):
  products = sorted([x*y for x, y in it.product(lst1, lst2)], reverse=True)
  return products[:n]


