def jacobsthal_num(n):
  if n == 1 or n == 2:
    return 1
  else:
    return jacobsthal_num(n-1) + jacobsthal_num(n-2) + 1