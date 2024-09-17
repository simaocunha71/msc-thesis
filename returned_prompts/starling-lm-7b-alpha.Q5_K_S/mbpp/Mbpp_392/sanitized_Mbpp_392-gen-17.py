def get_max_sum(n: int) -> int:
  if n < 0:
    return 0
  elif n < 2:
    return n
  else:
    return max(n + get_max_sum(n//2) + get_max_sum(n//3) + get_max_sum(n//4) + get_max_sum(n//5),n)