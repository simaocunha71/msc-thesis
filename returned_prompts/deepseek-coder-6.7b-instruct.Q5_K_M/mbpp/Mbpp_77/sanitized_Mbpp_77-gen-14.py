def is_Diff(n):
  n = str(n)
  return not (int(n[::2]) - int(n[1::2])) % 11