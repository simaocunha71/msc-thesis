
def unique_product(my_list):
  unique_elements = set()
  product = 1
  for num in my_list:
    if num not in unique_elements:
      unique_elements.add(num)
      product *= num
  return product


