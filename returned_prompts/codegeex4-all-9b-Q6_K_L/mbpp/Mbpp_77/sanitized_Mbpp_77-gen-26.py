def is_Diff(n):
  temp = n
  sum1 = 0
  sum2 = 0
  while temp > 0:
    sum1 += temp % 10
    temp //= 10
  temp = n
  while temp > 0:
    sum2 += temp % 100
    temp //= 100
  if abs(sum1 - sum2) % 11 == 0:
    return True
  else:
    return False