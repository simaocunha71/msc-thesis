def max_product_tuple(tup_list:list):
  max_prod = 0
  for i in range(len(tup_list)):
    for j in range(i+1,len(tup_list)):
      prod = abs(tup_list[i][0]*tup_list[i][1])*abs(tup_list[j][0]*tup_list[j][1])
      if prod > max_prod:
        max_prod = prod
  return max_prod