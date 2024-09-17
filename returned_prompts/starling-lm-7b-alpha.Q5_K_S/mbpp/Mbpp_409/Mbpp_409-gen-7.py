
def min_product_tuple(tuples:list) -> int:
  min_product = float("inf")
  for tup in tuples:
    for ele in tup:
      min_product = min(min_product, ele * tup[1-ele])
  return min_product


