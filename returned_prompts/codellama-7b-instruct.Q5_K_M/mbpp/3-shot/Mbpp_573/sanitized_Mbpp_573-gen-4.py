def unique_product(my_list):
  prod = 1
  for i in set(my_list):
    prod *= i
  return prod