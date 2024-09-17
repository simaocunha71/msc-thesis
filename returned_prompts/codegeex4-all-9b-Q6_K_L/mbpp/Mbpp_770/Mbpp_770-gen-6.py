def odd_num_sum(n: int) -> int:
  sum_ = 0
  for i in range(1, 2*n+1, 2):
    sum_ += i**4
  return sum_