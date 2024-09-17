
import math
def zero_count(arr):
  count_zero = 0
  count_non_zero = 0
  for i in arr:
    if i == 0:
      count_zero += 1
    else:
      count_non_zero += 1
  return count_zero / count_non_zero


