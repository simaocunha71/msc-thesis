def min_product_tuple(tuples: list):
  min_product = float('inf')
  for tuple1, tuple2 in tuples:
    product = tuple1 * tuple2
    if product < min_product:
      min_product = product
  return min_product

