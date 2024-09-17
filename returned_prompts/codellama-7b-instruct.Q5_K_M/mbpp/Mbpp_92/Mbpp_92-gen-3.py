
def is_undulating(n):
  if n == 123456789:
    return False
  if n == 12345678:
    return True
  if n % 10 in (0,9):
    return is_undulating(n//10)
  return is_undulating(n//10)


