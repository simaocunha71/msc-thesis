
def unique_product(lst):
  unique_lst = set(lst)
  product = 1
  for num in unique_lst:
    product *= num
  return product


