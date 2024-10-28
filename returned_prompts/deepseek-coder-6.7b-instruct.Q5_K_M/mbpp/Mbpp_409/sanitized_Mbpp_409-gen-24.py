def min_product_tuple(lst):
  products = [i[0]*i[1] for i in lst]
  return min(products)