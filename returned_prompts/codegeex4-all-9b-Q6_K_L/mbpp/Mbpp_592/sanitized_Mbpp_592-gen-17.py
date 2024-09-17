def sum_Of_product(n):
  sum_ = 0
  for i in range(n):
    sum_ += math.comb(n, i) * math.comb(n, i+1)
  return sum_