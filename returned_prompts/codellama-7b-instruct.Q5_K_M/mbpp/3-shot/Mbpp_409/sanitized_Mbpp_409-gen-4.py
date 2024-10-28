def min_product_tuple(my_list: list) -> int:
  min_product = 1
  for tup1, tup2 in zip(my_list, my_list[1:]):
    min_product = min(min_product, *tup1, *tup2)
  return min_product