
def bell_Number(n):
  if n == 0:
    return 1
  else:
    return sum([bell_Number(i) * bell_Number(n-i-1) for i in range(n)])


