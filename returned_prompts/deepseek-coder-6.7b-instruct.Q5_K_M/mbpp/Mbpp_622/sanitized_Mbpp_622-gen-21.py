def get_median(a, b, n):
  i = 0
  j = 0
  m1 = -1
  m2 = -1
  while(i + j <= n):
    if(i == n):
      m1 = m2
      m2 = b[0]
      b.pop(0)
      j += 1
    elif(j == n):
      m1 = m2
      m2 = a[0]
      a.pop(0)
      i += 1
    elif (a[0] < b[0]):
      m1 = m2
      m2 = a[0]
      a.pop(0)
      i += 1
    else:
      m1 = m2
      m2 = b[0]
      b.pop(0)
      j += 1
  return (m1 + m2)/2