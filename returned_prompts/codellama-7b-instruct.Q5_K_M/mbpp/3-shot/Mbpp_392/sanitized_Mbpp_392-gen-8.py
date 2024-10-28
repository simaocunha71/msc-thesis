def get_max_sum(n: int) -> int:
  if n <= 0:
    return 0
  if n == 1:
    return 1
  if n == 2:
    return 2
  if n == 3:
    return 3
  if n == 4:
    return 4
  if n == 5:
    return 5
  else:
    return max(n + get_max_sum(n//2) + get_max_sum(n//3) + get_max_sum(n//4) + get_max_sum(n//5), n)