def square_Sum(n: int) -> int:
  square_sum = sum([i*i for i in range(1, n*2, 2)])
  return square_sum