def max_product_tuple(num_tup_list):
  max_prod = 0
  for i in range(len(num_tup_list)):
    for j in range(i, len(num_tup_list)):
      prod = abs(num_tup_list[i][0] * num_tup_list[i][1]) * abs(num_tup_list[j][0] * num_tup_list[j][1])
      if prod > max_prod:
        max_prod = prod
  return max_prod