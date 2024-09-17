import math
def multiply_num(num_list):
  result = 1
  for num in num_list:
    result *= num
  result /= len(num_list)
  return result