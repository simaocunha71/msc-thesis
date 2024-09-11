import math
def zero_count(lst):
  count = 0
  for i in lst:
    if i == 0:
      count += 1
  ratio = count / len(lst)
  return ratio