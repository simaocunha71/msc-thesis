def difference(n):
  return sum([i**3 for i in range(1, n+1)]) - sum([i for i in range(1, n+1)])