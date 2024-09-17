def catalan_number(n: int) -> int:
  if n<0:
    return 0
  if n==0:
    return 1
  return sum(catalan_number(i)*catalan_number(n-i-1) for i in range(n))