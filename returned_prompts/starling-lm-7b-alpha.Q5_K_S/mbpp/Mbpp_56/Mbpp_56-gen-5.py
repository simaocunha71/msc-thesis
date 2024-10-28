
def check(n: int):
  if n == 2 * int(str(n)[::-1]) - 1:
    return True
  else:
    return False


