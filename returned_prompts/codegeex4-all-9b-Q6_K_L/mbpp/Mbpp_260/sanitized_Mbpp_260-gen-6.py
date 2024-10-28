def newman_prime(n):
  def is_prime(num):
    if num < 2:
      return False
    for i in range(2, int(num ** 0.5) + 1):
      if num % i == 0:
        return False
    return True

  def newman_sequence(n):
    sequence = [2]
    for _ in range(n):
      sequence.append(sequence[-1] + sum(sequence[:-1]))
    return sequence

  count = 0
  i = 1
  while True:
    sequence = newman_sequence(i)
    for prime in sequence:
      if is_prime(prime):
        count += 1
        if count == n:
          return prime
    i += 1