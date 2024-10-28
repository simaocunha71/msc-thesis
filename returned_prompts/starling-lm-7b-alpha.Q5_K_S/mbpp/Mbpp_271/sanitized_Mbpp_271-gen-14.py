def even_Power_Sum(n: int) -> int:
  sum_even_pow = sum([i**5 for i in range(1,n+1) if i%2==0])
  return sum_even_pow