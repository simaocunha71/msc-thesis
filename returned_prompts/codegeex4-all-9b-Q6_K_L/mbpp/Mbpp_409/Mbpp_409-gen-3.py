def min_product_tuple(tuples: list) -> int:
  return min(t[0]*t[1] for t in tuples)