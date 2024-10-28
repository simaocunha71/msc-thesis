def sum(a: int, b: int) -> int:
  common_divisors = [x for x in range(1, min(a,b)+1) if a % x == 0 and b % x == 0]
  return sum(common_divisors)