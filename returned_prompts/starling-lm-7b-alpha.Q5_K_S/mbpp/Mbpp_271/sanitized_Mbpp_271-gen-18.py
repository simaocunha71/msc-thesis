def even_Power_Sum(n: int) -> int:
  sum_ = 0
  for i in range(n):
    sum_ += (i+1)**5
  return sum_