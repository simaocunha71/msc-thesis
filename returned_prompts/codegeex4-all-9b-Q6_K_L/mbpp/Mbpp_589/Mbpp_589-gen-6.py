def perfect_squares(n1: int,n2: int) -> list:
  return [i for i in range(n1,n2+1) if int(math.sqrt(i))**2 == i]

