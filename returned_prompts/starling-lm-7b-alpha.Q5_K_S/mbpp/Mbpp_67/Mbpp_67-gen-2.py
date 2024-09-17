
def bell_number(n: int) -> int:
  if n == 0:
    return 1
  elif n == 1:
    return 2
  else:
    return sum(bell_number(i) for i in range(n))


