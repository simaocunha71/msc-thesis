
def sum_common_divisors(a: int, b: int) -> int:
  factors_of_a = set(range(1, a + 1))
  factors_of_b = set(range(1, b + 1))

  for factor in factors_of_a:
      if factor in factors_of_b:
          factors_of_a.remove(factor)
          factors_of_b.remove(factor)
          break

  return sum(factors_of_a) + sum(factors_of_b)


