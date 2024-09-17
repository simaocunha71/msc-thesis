
def is_product_even(my_list):
  product = 1
  for num in my_list:
    product *= num
  if product % 2 == 0:
    return True
  else:
    return False


