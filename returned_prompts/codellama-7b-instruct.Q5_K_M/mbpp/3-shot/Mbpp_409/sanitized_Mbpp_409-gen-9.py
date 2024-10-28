def min_product_tuple(tuple_list):
  min_product = None
  for i in tuple_list:
    if not min_product:
      min_product = i[1]
    else:
      if min_product > i[1]:
        min_product = i[1]
  return min_product