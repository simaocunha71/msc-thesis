def is_product_even(my_list):
  if len(my_list) == 0:
    return False
  result = 1
  for num in my_list:
    result *= num
  return result % 2 == 0