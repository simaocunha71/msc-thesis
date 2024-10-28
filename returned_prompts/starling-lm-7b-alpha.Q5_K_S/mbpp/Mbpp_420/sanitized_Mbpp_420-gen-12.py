def cube_Sum(n: int) -> int:
  cube_sum = sum([i**3 for i in range(1,n+1) if i%2==0])
  return cube_sum