import math
def zero_count(arr: list) -> float:
  count = 0
  for x in arr:
    if x == 0:
      count += 1
  return count / len(arr)