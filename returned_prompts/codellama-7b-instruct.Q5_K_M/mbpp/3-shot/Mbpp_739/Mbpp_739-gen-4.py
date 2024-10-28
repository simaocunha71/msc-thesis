
def find_Index(n: int) -> int:
  triangular_numbers = []
  for i in range(1,n+1):
    triangular_numbers.append(i*(i+1)//2)
  return triangular_numbers.index(min(triangular_numbers))


