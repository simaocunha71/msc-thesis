def sum_Of_product(n:int):
  if n == 0:
    return 0
  if n == 1:
    return 1
  num = 1
  den = 1
  sum_ = 1
  for _ in range(2, n+1):
    num *= (n-1)
    num //= _
    den *= (_-1)
    den *= _
    sum_ += num//den
  return sum_