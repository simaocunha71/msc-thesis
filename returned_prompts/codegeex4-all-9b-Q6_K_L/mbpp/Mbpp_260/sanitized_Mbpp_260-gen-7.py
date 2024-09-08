def newman_prime(n):
  def is_newman_prime(p):
    def continued_fraction(a, b):
      if a == 0 or b == 0:
        return []
      else:
        return [b // a] + continued_fraction(a, b % a)

    def convergents(cf):
      if not cf:
        return []
      else:
        c0, c1 = 0, 1
        d0, d1 = 1, cf[0]
        for _ in cf[1:]:
          c0, c1 = c1, _ * c1 + c0
          d0, d1 = d1, _ * d1 + d0
          yield (c1, d1)

    cf = continued_fraction(1, p - 1)
    convergents_ = list(convergents(cf))
    return any(c1 / d1 == p for c1, d1 in convergents_)

  primes = [2, 3]
  for p in range(5, 10**6, 2):
    if all(p % q != 0 for q in primes):
      primes.append(p)
      if is_newman_prime(p):
        n -= 1
        if n == 0:
          return p

  return None