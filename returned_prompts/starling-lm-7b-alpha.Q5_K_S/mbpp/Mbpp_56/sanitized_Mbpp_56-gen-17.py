def check(n: int):
  if (n*2 - 1) == int(str(n)[::-1]):
    return True
  else:
    return False