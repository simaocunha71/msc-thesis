
def max_product_tuple(test_tups):
  max_product = 0
  for tup in test_tups:
    max_product = max(max_product, tup[0] * tup[1], abs(tup[0] - tup[1]))
  return max_product


