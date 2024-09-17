
def sum_common_divisors(a: int, b: int) -> int:
  i = 1
  while i <= min(a, b):
    if a % i == 0 and b % i == 0:
      sum = i + sum_common_divisors(a, b, i + 1)
    i += 1
  return sum


def sum_common_divisors(a: int, b: int, i: int = 1):
  if i <= min(a, b):
    if a % i == 0 and b % i == 0:
      sum = i + sum_common_divisors(a, b, i + 1)
    i += 1
  return sum


def sum_common_divisors(a: int, b: int) -> int:
  i = 1
  while i <= min(a, b):
    if a % i == 0 and b % i == 0:
      sum = i + sum_common_divisors(a, b, i + 1)
    i += 1
  return sum


def sum_common_divisors(a: int, b: int) -> int:
  i = 1
  while i <= min(a, b):
    if a % i == 0 and b % i == 0:
      sum = i + sum_common_divisors(a, b, i + 1)
    i += 1
  return sum


