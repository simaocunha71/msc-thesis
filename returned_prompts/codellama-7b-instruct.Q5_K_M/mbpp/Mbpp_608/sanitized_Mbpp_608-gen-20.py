def bell_Number(n: int) -> int:
  if n == 1:
    return 1
  return sum(bell_Number(i) for i in range(n))