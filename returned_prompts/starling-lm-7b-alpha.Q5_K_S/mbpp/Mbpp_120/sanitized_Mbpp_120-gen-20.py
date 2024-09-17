def max_product_tuple(tuple_list:list)->int:
  max_product = 0
  for tup in tuple_list:
    if tup[0] * tup[1] < 0:
      max_product = max(max_product, tup[0] * tup[1])
    else:
      max_product = max(max_product, tup[0] * tup[1], abs(tup[0]) * abs(tup[1]))
  return max_product