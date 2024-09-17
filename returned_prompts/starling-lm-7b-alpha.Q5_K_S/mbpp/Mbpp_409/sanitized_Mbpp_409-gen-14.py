def min_product_tuple(test_list: list) -> int:
  min_product = 100000000
  for i in range(len(test_list)):
    if test_list[i][0] * test_list[i][1] < min_product:
      min_product = test_list[i][0] * test_list[i][1]
  return min_product