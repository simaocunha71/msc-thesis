
def odd_num_sum(n):
  total = 0
  for num in range(1, n*2+1, 2):
    total += num ** 4
  return total


