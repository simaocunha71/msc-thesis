
from statistics import mean, median
def zero_count(arr):
  non_zero = sum(filter(lambda x: x != 0, arr))
  zero = sum(filter(lambda x: x == 0, arr))
  return zero / non_zero


