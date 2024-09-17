
def check(n: int) -> bool:
  if n % 2 == 0:
    n_reversed = int(str(n)[::-1])
    if n_reversed == n - 1:
      return True
    else:
      return False
  else:
    return False


