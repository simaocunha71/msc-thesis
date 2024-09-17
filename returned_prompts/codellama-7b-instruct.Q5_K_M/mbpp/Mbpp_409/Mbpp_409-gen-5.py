
def min_product_tuple(my_tuple_list: list) -> int:
  min_product = 0
  for i in range(len(my_tuple_list)):
    for j in range(i+1,len(my_tuple_list)):
      if my_tuple_list[i][0] * my_tuple_list[j][1] < my_tuple_list[j][0] * my_tuple_list[i][1]:
        min_product = my_tuple_list[i][0] * my_tuple_list[j][1]
      elif my_tuple_list[i][0] * my_tuple_list[j][1] > my_tuple_list[j][0] * my_tuple_list[i][1]:
        min_product = my_tuple_list[j][0] * my_tuple_list[i][1]
      else:
        continue
  return min_product


