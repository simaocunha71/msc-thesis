def min_product_tuple(tuples: list) -> int:
  product_list = [t[0]*t[1] for t in tuples]
  return min(product_list)