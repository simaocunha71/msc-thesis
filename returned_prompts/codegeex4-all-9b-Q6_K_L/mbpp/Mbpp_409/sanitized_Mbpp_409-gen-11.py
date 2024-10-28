def min_product_tuple(tuples: list) -> int:
  min_product = float('inf')
  for tup in tuples:
    min_product = min(min_product, tup[0] * tup[1])
  return min_product