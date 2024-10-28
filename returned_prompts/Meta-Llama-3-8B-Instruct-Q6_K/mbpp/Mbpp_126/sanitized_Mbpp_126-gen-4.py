def sum(a, b):
  common_divisors = [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]
  return sum(common_divisors)  # or sum(set(common_divisors)) to avoid duplicates