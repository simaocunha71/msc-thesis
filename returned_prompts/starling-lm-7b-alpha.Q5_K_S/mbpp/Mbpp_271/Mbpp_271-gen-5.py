
def even_Power_Sum(n):
  result = sum([i**5 for i in range(1, n+1) if i % 2 == 0])
  return result


