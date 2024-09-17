def max_product_tuple(tuples: list) -> int:
  max_product = -float('inf')
  for tup in tuples:
    if tup[0] * tup[1] > max_product:
      max_product = tup[0] * tup[1]
  return max_product