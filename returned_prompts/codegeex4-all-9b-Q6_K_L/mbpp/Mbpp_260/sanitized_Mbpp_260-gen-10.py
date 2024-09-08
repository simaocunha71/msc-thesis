def newman_prime(n):
  def newman_sequence(a0, a1):
    yield a0
    yield a1
    while True:
      a0, a1 = a1, a0 + a1
      yield a1

  def is_prime(n):
    if n < 2:
      return False
    for i in range(2, int(n ** 0.5) + 1):
      if n % i == 0:
        return False
    return True

  count = 0
  for a0, a1 in enumerate(newman_sequence(2, 3), 2):
    if is_prime(a0) and is_prime(a1):
      count += 1
      if count == n:
        return a0

  raise ValueError(f"Failed to find the {n}th newman–shanks–williams prime number")