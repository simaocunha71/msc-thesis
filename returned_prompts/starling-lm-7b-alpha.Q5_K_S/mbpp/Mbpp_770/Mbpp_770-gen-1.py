
def odd_num_sum(n: int) -> int:
  sum_odd = 0
  for i in range(1,2*n, 2):
    sum_odd += i**4
  return sum_odd


