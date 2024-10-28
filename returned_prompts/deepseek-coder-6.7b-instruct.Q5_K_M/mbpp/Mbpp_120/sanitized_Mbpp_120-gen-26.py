def max_product_tuple(tuples_list: list) -> int:
  products = [abs(t[0]*t[1]) for t in tuples_list]
  return max(products)