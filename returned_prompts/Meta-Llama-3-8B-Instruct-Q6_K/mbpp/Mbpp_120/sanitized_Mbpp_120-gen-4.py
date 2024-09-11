def max_product_tuple(tuples_list):
  max_product = 0
  for i in range(len(tuples_list)):
    for j in range(i+1, len(tuples_list)):
      product = abs(tuples_list[i][0]*tuples_list[i][1] - tuples_list[j][0]*tuples_list[j][1])
      if product > max_product:
        max_product = product
  return max_product