def divisor(n):
  i = 1
  count = 0
  while i <= n:
    if n % i == 0:
      count += 1
    i += 1
  return count