
def odd_num_sum(n: int) -> int:
  sum = 0
  for i in range(1, n+1):
    if i % 2 == 1:
      sum += i ** 4
  return sum


