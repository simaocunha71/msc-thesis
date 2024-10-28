def bell_Number(n):
  if n == 0:
    return 1
  elif n == 1:
    return 1
  else:
    return 2**n + bell_Number(n-1)