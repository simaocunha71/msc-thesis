
def odd_num_sum(n: int) -> int:
  num_sum = 0
  for i in range(1, 2 * n + 1, 2):
    num_sum += i ** 4
  return num_sum


