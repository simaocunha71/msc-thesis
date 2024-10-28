def min_product_tuple(tuple_list:list) -> int:
  min_product = float("inf")
  for i in range(len(tuple_list)):
    for j in range(i+1, len(tuple_list)):
      min_product = min(min_product, tuple_list[i][0]*tuple_list[i][1]*tuple_list[j][0]*tuple_list[j][1])
  return min_product