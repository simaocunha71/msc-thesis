import math
def multiply_num(test_tup):
  product = 1
  for num in test_tup:
    product *= num
  return product / len(test_tup)