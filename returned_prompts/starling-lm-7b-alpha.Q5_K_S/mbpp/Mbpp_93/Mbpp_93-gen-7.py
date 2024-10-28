
def power(a: int,b: int) -> int:
  if b == 0:
    return 1
  if b % 2 == 0:
    return power(a ** 2, b // 2)
  else:
    return a * power(a ** 2, b // 2)


