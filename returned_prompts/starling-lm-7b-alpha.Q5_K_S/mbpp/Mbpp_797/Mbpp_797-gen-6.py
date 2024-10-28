
def sum_in_range(l,r):
  odd_sum = 0
  for i in range(l,r+1):
    if i % 2 != 0:
      odd_sum += i
  return odd_sum


