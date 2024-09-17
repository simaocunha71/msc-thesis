
def square_Sum(n: int) -> int:
  squares = [i**2 for i in range(1,n+1) if i%2==0]
  return sum(squares)


