def is_product_even(my_list):
  product = 1
  for i in my_list:
    product *= i
  if product % 2 == 0:
    return True
  else:
    return False