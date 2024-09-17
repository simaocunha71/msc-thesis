def is_product_even(my_list):
  result = 1
  for num in my_list:
    result *= num
  return result % 2 == 0