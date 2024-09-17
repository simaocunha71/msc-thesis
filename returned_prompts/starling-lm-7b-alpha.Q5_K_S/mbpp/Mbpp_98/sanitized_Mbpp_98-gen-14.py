import math
def multiply_num(num_tup):
  product = 1
  for i in num_tup:
    product *= i
  return product/len(num_tup)