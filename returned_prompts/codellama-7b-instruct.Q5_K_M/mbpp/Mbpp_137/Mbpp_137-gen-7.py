
import math
def zero_count(my_list):
  count = 0
  for i in my_list:
    if i == 0:
      count += 1
  return count / len(my_list)


