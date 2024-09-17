
def odd_num_sum(n):
  return sum(i**4 for i in range(2*n) if i%2 != 0)


