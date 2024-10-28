def unique_product(my_list: list):
  unique_list = list(set(my_list))
  product = 1
  for num in unique_list:
    product *= num
  return product