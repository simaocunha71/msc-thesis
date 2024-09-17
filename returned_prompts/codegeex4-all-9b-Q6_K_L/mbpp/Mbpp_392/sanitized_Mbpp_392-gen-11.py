def get_max_sum(n):
  if n == 1:
    return 1
  else:
    return max((get_max_sum(int(n/2)) + get_max_sum(int(n/3)) + get_max_sum(int(n/4)) + get_max_sum(int(n/5))), n)