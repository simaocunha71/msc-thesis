
def odd_num_sum(n: int) -> int:
  result = 0
  for i in range(1, n+1):
    result += i**4
  return result


