
def max_product_tuple(lst):
  product_list = [abs(a*b) for (a, b) in lst]
  return max(product_list)


