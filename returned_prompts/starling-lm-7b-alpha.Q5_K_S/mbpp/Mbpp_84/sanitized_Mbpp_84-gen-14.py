def sequence(n: int) -> int:
  if n == 0:
    return 0
  if n == 1:
    return 1
  if n == 2:
    return 2
  if n == 3:
    return 5
  if n == 4:
    return 8
  if n % 2 == 0:
    return sequence(n-1) + sequence(n-2)
  if n % 2 == 1:
    return sequence(n-1) + 3 + sequence(n-3)