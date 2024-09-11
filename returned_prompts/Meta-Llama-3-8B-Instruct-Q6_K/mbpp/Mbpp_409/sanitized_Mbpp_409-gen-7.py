def min_product_tuple(tuples):
  return min(a*b for a, b in tuples) if tuples else None