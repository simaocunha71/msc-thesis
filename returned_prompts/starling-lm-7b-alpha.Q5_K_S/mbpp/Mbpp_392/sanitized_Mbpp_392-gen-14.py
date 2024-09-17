def get_max_sum(n):
  if n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 3
  elif n == 4:
    return 4
  else:
    return max((get_max_sum(n//2) + get_max_sum(n//3) + get_max_sum(n//4) + get_max_sum(n//5)), n)