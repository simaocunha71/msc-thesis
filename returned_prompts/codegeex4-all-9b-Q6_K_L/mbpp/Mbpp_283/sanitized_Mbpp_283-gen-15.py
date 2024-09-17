def validate(n: int) -> bool:
  n = str(n)
  for i in n:
    if int(i) > n.count(i):
      return False
  return True