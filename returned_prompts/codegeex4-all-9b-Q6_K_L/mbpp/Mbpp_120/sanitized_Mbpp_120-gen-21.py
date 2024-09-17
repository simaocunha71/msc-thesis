def max_product_tuple(tuples: list) -> int:
  max_product = 0
  for tup in tuples:
    max_product = max(max_product, abs(tup[0]*tup[1]))
  return max_product