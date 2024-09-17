def is_undulating(n):
  if str(n) == str(n)[::-1]:
    return False
  else:
    s = list(str(n))
    if s == s[::-1]:
      return True
    else:
      return False