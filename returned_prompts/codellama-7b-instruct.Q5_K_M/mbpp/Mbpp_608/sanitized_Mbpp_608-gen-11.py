def bell_Number(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return sum(bell_Number(i) * bell_Number(n-i-1) for i in range(n))