def check(n):
  reverse_num = int(str(n)[::-1])
  if n == reverse_num * 2 - 1:
    return True
  return False