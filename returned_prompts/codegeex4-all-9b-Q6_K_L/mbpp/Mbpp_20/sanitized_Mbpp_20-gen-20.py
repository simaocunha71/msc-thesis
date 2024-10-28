def is_woodall(n: int) -> bool:
  if n <= 1:
    return False
  sum = 0
  i = 2
  while i * i <= n:
    if n % i:
      i += 1
    else:
      n //= i
      sum += i - 1
  if n > 1:
    sum += n - 1
  return sum == n