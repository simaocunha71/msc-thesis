
def even_Power_Sum(n: int) -> int:
  sum = 0
  for i in range(2, n+1):
    sum += (i**5)
  return sum


