def closest_num(n):
  return next(i for i in range(n-1,0,-1) if i % 2 == n % 2)