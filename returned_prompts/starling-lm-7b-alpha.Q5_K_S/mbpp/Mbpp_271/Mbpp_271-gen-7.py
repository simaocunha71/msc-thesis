
def even_Power_Sum(n):
  even_nums = [i**5 for i in range(1, n+1) if i%2==0]
  return sum(even_nums)


