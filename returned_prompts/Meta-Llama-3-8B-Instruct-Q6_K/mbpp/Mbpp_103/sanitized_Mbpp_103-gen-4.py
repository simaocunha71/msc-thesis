def eulerian_num(n, m):
  return math.factorial(n) // (math.factorial(m) * math.factorial(n - m)) * m