import itertools as it
def large_product(lst1, lst2, n):
  products = [i*j for i, j in it.product(lst1, lst2)]
  products.sort(reverse=True)
  return products[:n]