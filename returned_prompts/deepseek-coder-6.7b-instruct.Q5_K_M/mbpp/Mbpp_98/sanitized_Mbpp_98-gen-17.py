import math
def multiply_num(numbers):
  product = 1
  for num in numbers:
    product *= num
  return product / len(numbers)