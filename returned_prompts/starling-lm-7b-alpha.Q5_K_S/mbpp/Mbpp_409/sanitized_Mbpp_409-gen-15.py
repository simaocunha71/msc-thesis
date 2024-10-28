def min_product_tuple(tuple_list:list)->int:
  min_product = min(tuple_list,key=lambda x: min(x[0]*x[1]))
  return min_product[0]*min_product[1]