
def unique_product(lst):
  lst = list(set(lst))
  product = 1
  for i in lst:
    product *= i
  return product


