def sum_in_range(l,r):
  sum = 0
  for num in range(l, r+1):
    if num % 2 != 0:
      sum += num
  return sum

