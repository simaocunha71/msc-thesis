def eulerian_num(n, m):
  result = 0
  for i in range(1, n+1):
    for j in range(1, m+1):
      if i <= j:
        result += 1
  return result