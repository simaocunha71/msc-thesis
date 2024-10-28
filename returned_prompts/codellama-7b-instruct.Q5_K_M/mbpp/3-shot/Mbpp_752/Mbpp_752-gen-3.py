
def jacobsthal_num(n: int) -> int:
  if n == 0:
    return 0
  if n == 1:
    return 1
  else:
    return jacobsthal_num(n-1) + jacobsthal_num(n-2)


