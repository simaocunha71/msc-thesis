def is_woodall(n):
  def woodall(n):
    if n == 1:
      return True
    if n % 2 == 0:
      return woodall(n // 2)
    return is_prime(n)
  def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
      if n % i == 0:
        return False
    return True
  return woodall(n) and is_prime(n)

