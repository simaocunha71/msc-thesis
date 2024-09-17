def min_product_tuple(tuples: list) -> int:
  min_product = float('inf')
  for tup in tuples:
    product = tup[0] * tup[1]
    if product < min_product:
      min_product = product
  return min_product