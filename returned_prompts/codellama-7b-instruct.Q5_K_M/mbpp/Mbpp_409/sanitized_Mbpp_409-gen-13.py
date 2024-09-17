def min_product_tuple(my_list):
  return min(my_list, key=lambda x: x[1] * x[0])[1] * min(my_list, key=lambda x: x[1] * x[0])[0]