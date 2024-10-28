
import math
def zero_count(arr):
  count = 0
  for i in arr:
    if i == 0:
      count += 1

  return count / len(arr)


