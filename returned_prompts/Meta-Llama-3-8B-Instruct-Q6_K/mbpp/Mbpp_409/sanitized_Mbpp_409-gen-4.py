def min_product_tuple(lst):
  min_product = float('inf')
  for i in lst:
    min_product = min(min_product, i[0]*i[1])
  return min_product