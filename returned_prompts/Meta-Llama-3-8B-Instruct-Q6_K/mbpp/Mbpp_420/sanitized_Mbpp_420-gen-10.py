def cube_Sum(n):
  return sum([i**3 for i in range(2, 2*n+1, 2)])  # 2*n+1 is used to get the last even number