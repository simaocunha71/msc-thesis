
def bell_number(n):
  if n <= 0:
    return 1
  return sum(bell_number(i) for i in range(n))


