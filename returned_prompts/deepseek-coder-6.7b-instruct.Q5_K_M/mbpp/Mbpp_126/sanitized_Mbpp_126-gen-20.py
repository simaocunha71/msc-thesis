def sum(n, m):
  sum = 0
  for i in range(1, min(n, m) + 1):
    if n % i == 0 and m % i == 0:
      sum += i
  return sum