def cube_Sum(n: int) -> int:
  if n==0:
    return 0
  return n**3 + cube_Sum(n-2)